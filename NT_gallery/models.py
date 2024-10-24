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
    LifestyleRating = models.CharField(max_length=255)

    def __str__(self):
        return self.LifestyleRating
    

class Health_support(models.Model):
    name = models.CharField(max_length=255)
    clinical_file = models.FileField(upload_to='documents/', blank=True, null=True)
    summary_file = models.FileField(upload_to='documents/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class Side_effects(models.Model):
    name = models.CharField(max_length=255)
    clinical_file = models.FileField(upload_to='documents/', blank=True, null=True)
    summary_file = models.FileField(upload_to='documents/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class Fortify(models.Model):
    name = models.CharField( max_length=255 )
    clinical_file = models.FileField(upload_to='documents/', blank=True, null=True)
    summary_file = models.FileField(upload_to='documents/', blank=True, null=True)
    
    def __str__(self):
        return self.name


class Health_Benefits(models.Model):
    product_name = models.CharField(max_length=255,null = True)
    health_support = models.ManyToManyField(Health_support)
    Side_effects = models.ManyToManyField(Side_effects)
    Fortify = models.ManyToManyField(Fortify)

    def __str__(self):
        return self.product_name



# Product model to relate categories
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    strength = models.IntegerField
    pharmacy_grouping = models.ManyToManyField(PharmacyGrouping)
    brand = models.ManyToManyField(Brand)
    age_range = models.ForeignKey(AgeRange, on_delete=models.CASCADE, null = True)
    gender = models.ManyToManyField(Gender)
    lifestyle = models.ManyToManyField(Lifestyle)
    dosage_form = models.ManyToManyField(DosageForm)
    lifestyle_rating = models.ManyToManyField(LifestyleRating)
    health_benefits = models.ManyToManyField(Health_Benefits)
    description = models.TextField()
    main_image = models.ImageField(upload_to='product_images/main',null=True)
    side_image_1 = models.ImageField(upload_to='product_images/secondary', blank=True, null=True)
    side_image_2 = models.ImageField(upload_to='product_images/secondary', blank=True, null=True)
    side_image_3 = models.ImageField(upload_to='product_images/secondary', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def _str_(self):
        return self.name


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