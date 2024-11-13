from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import requests

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
    name = models.CharField(max_length=255, default = 0, null = True)
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
# class Lifestylerating(models.Model):
#     LifestyleRating = models.CharField(max_length=255, null=True)
        
#     def _str_(self):
#             return self.LifestyleRating
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, blank=True)
    sub_categories = models.JSONField(default=list)  # A flexible array-like field for subcategories
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    strength = models.CharField(max_length=255,null=True)
    description = models.TextField(null=True, blank=True)
    pictures = models.JSONField(default=dict)  # Store images paths in a JSON field
    fortify = models.OneToOneField('Fortify', on_delete=models.CASCADE, related_name='product', null=True)
    side_effect = models.OneToOneField('Side_effects', on_delete=models.CASCADE, related_name='product', null=True)
    health_support = models.OneToOneField('Health_support', on_delete=models.CASCADE, related_name='product', null=True)
    # fortify = models.OneToOneField(FortifyOption, on_delete=models.CASCADE, related_name='product', null=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE,null = True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_from_api(cls):
        """
        Fetch product data from an external API and return the product data as a dictionary.
        """
        response = requests.get("https://hls-vr1z.onrender.com/api/product")
        if response.status_code == 200:
            data = response.json()
            return cls.process_product_data(data)
        else:
            return None  # Or handle errors as needed

    @staticmethod
    def process_product_data(data):
        """
        Process the API response and return the product data in a structured format.
        """
        # Here we return a dictionary of the data fetched
        product_data = {
            'name': data.get('name'),
            # 'generic_name': data.get('generic_name'),
            'price': data.get('price'),
            'strength': data.get('strength'),
            'description': data.get('description'),
            'main_image': data.get('main_image'),
            'side_image_1': data.get('side_image_1'),
            'side_image_2': data.get('side_image_2'),
            'side_image_3': data.get('side_image_3'),
            # 'pharmacy_grouping': data.get('pharmacy_grouping', []),  # Example: list of IDs
            # 'brand': data.get('brand', []),  # Example: list of IDs
            # 'age_range': data.get('age_range'),
            # 'gender': data.get('gender', []),  # Example: list of IDs
            # 'lifestyle': data.get('lifestyle', []),  # Example: list of IDs
            # 'dosage_form': data.get('dosage_form', []),  # Example: list of IDs
        }
        return product_data
    
    
        

class Health_support(models.Model):
    name =  models.CharField(max_length=255, null = True)
    # nutrient = models.ForeignKey(Product, on_delete=models.CASCADE, null = True)
    health_condition = models.CharField(max_length=255)
    strength = models.CharField(max_length=255,null = True)
    times_per_day = models.IntegerField(null = True)
    length_of_use = models.CharField(max_length=255,null = True)
    clinical_file = models.FileField(upload_to='documents/', blank=True, null=True)
    summary_file = models.FileField(upload_to='summary_doc/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.nutrient.name} - {self.health_condition}" if self.nutrient else 'No nutrient specified'
    
class Side_effects(models.Model):
    name =  models.CharField(max_length=255, null = True)
    # nutrient = models.ForeignKey(Product, on_delete=models.CASCADE, null = True)
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
    # nutrient = models.ForeignKey(Product, on_delete=models.CASCADE, null = True)
    name =  models.CharField(max_length=255, null = True)
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

    def save(self, *args, **kwargs):
        # API call before saving
        response = requests.post('https://example.com/api/health_support', data={
            'name': self.name,
            'health_condition': self.health_condition,
            'strength': self.strength,
            'times_per_day': self.times_per_day,
            'length_of_use': self.length_of_use,
        })
        
        # Check if the request was successful
        if response.status_code == 200:
            print("API call successful:", response.json())
        else:
            print("API call failed:", response.status_code, response.text)

        super().save(*args, **kwargs) 
  
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


