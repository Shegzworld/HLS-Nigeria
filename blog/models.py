from django.db import models
from django.utils.text import slugify
from PIL import Image
from io import BytesIO

# Create your models here.
from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    author_img = models.ImageField(upload_to='author_images/', null = True)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    



class Blog(models.Model):
    title = models.CharField(max_length=255) 
    category = models.ManyToManyField(Category)
    highlight = models.TextField(null=True, blank=True)
    image_1 = models.ImageField(upload_to='blog_images/',null=True, blank=True)
    content_1 = models.TextField(null=True, blank=True)
    image_2 = models.ImageField(upload_to='blog_images/',null=True, blank=True)
    content_2 = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)  # Make sure the slug is unique and can be empty initially
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    # author = models.OneToOneField(Author, on_delete=models.CASCADE, null=True, blank=True, related_name='blog')
    # bio = models.OneToOneField(Author, on_delete=models.CASCADE, null=True, blank=True, related_name='blog')

    def save(self, *args, **kwargs):
        # Only regenerate the slug if the title has changed (during an update)
        if not self.slug:  # If slug doesn't exist (i.e., on create)
            self.slug = slugify(self.title)  # Convert the title to a slug
        elif self.pk:  # If the object already exists and is being updated
            original = Blog.objects.get(pk=self.pk)
            if original.title != self.title:  # Check if the title has changed
                self.slug = slugify(self.title)  # Update slug based on new title

        # Only resize image if it has been uploaded (i.e., not a default image)
        if self.image_1 and hasattr(self.image_1, 'name'):
            img = Image.open(self.image_1)

            # Check if resizing is needed (resize only if width or height > 150px)
            if img.height > 150 or img.width > 150:
                output_size = (150, 150)
                img.thumbnail(output_size)

                # Save the resized image to an in-memory buffer
                img_io = BytesIO()
                img.save(img_io, img.format)
                img_io.seek(0)

                # Save the resized image to the ImageField (S3 backend will take care of uploading)
                self.image_1.save(self.image_1.name, img_io, save=False)

        if self.image_2 and hasattr(self.image_2, 'name'):
            img2 = Image.open(self.image_2)

            # Check if resizing is needed (resize only if width or height > 150px)
            if img2.height > 150 or img2.width > 150:
                output_size = (150, 150)
                img2.thumbnail(output_size)

                # Save the resized image to an in-memory buffer
                img_io = BytesIO()
                img2.save(img_io, img2.format)
                img_io.seek(0)

                # Save the resized image to the ImageField (S3 backend will take care of uploading)
                self.image_2.save(self.image_2.name, img_io, save=False)

        # Call the parent class's save method to save the model
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title  # Return the title of the blog post for display in admin
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.blog.title} - {self.author}"
    

