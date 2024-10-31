from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# 1. Pharmacy Grouping
class PharmacyGrouping(models.Model):
    PharmacyGrouping = models.CharField(max_length=255)

    def __str__(self):
        return self.PharmacyGrouping


# 2. Brands
class Brand(models.Model):
    Brand_Name = models.CharField(max_length=255)

    def __str__(self):
        return self.Brand_Name


    
class AgeRange(models.Model):
    name = models.CharField(max_length=255, default = 0)
    min_age = models.IntegerField()
    max_age = models.IntegerField()

    def __str__(self):
        return self.name



# 4. Gender
class Gender(models.Model):
    Gender = models.CharField(max_length=255)

    def __str__(self):
        return self.Gender


# 8. Lifestyle
class Lifestyle(models.Model):
    LifestyleType = models.CharField(max_length=255)

    def __str__(self):
        return self.LifestyleType


# 10. Dosage Forms
class DosageForm(models.Model):
    DosageForm = models.CharField(max_length=255)

    def __str__(self):
        return self.DosageForm

# 11. Lifestyle Rating
class LifestyleRating(models.Model):
    LifestyleRating = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.LifestyleRating
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    Generic_name = models.CharField(max_length=255, null = True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null = True)
    strength = models.IntegerField(blank =True,null = True)
    pharmacy_grouping = models.ManyToManyField(PharmacyGrouping)
    brand = models.ManyToManyField(Brand)
    age_range = models.ForeignKey(AgeRange, on_delete=models.CASCADE, null = True)
    gender = models.ManyToManyField(Gender)
    lifestyle = models.ManyToManyField(Lifestyle)
    dosage_form = models.ManyToManyField(DosageForm)
    lifestyle_rating = models.ManyToManyField(LifestyleRating)
    description = models.TextField(null = True)
    main_image = models.ImageField(upload_to='product_images/main',null=True)
    side_image_1 = models.ImageField(upload_to='product_images/secondary', blank=True, null=True)
    side_image_2 = models.ImageField(upload_to='product_images/secondary', blank=True, null=True)
    side_image_3 = models.ImageField(upload_to='product_images/secondary', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        return self.name

class Health_support(models.Model):
    nutrient = models.ForeignKey(Product, on_delete=models.CASCADE, null = True)
    health_condition = models.CharField(max_length=255)
    strength = models.CharField(max_length=255,null = True)
    times_per_day = models.IntegerField(null = True)
    length_of_use = models.CharField(max_length=255,null = True)
    clinical_file = models.FileField(upload_to='documents/', blank=True, null=True)
    summary_file = models.FileField(upload_to='summary_doc/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.nutrient.name} - {self.health_condition}" if self.nutrient else 'No nutrient specified'
    
class Side_effects(models.Model):
    nutrient = models.ForeignKey(Product, on_delete=models.CASCADE, null = True)
    medication = models.CharField(max_length=255)
    strength = models.CharField(max_length=255,null = True)
    tabs = models.IntegerField(null = True)
    times_per_day = models.IntegerField(null = True)
    length_of_use = models.CharField(max_length=255,null = True)
    clinical_file = models.FileField(upload_to='documents/', blank=True, null=True)
    summary_file = models.FileField(upload_to='summary_doc/', blank=True, null=True)
    
    def __str__(self):
        return self.medication

class Fortify(models.Model):
    nutrient = models.ForeignKey(Product, on_delete=models.CASCADE, null = True)
    organ = models.CharField( max_length=255, null=True )
    strength = models.CharField(max_length=255, null = True)
    tabs = models.IntegerField(null = True)
    times_per_day = models.IntegerField(null = True)
    length_of_use = models.CharField(max_length=255,null = True)
    clinical_file = models.FileField(upload_to='documents/', blank=True, null=True)
    summary_file = models.FileField(upload_to='summary_doc/', blank=True, null=True)
    
    def __str__(self):
        return str(self.nutrient) if self.nutrient else 'No nutrient specified'
    
class Health_Benefits(models.Model):
    name = models.CharField( max_length=255, null = True)
    nutrient = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='health_benefits', null = True)
    health_support = models.OneToOneField(Health_support, on_delete=models.CASCADE, related_name='health_benefits',blank=True, null = True)
    Side_effects = models.OneToOneField(Side_effects, on_delete=models.CASCADE, related_name='health_benefits',blank=True, null = True)
    Fortify = models.OneToOneField(Fortify, on_delete=models.CASCADE, related_name='health_benefits',blank=True, null = True)

    def __str__(self):
        return str(self.nutrient) if self.nutrient else 'No nutrient specified'
  
class ProductReview(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE,null = True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = 'product_review')
    # rating = models.IntegerField(choices=[1, 2, 3, 4, 5])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product}{' reviews by'} - {self.user.username}"


# class Prof_Pack:
#     image_1 = models.ImageField()
#     image_2 = models.ImageField()

# class Doctor_Pack:
#     pass

# class HLS_Pack:
#     pass

# class ECO_Pack:
#     pass

# class Everyman_Pack:
#     pass