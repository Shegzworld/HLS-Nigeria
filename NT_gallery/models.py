from django.db import models
# from django.contrib.auth.models import User
from user.models import CustomUser as User

from django.utils import timezone

# 1. Pharmacy Grouping
class PharmacyGrouping(models.Model):
    NAME_CHOICES = [
        ('Single Vitamins', 'Single Vitamins'),
        ('Multi Vitamins', 'Multi Vitamins'),
        ('Multi Minerals', 'Multi Minerals'),
        ('Herbal Supplements', 'Herbal Supplements'),
        ('Essential Fatty Acids', 'Essential Fatty Acids'),
        ('Amino Acids', 'Amino Acids'),
        ('Tonics', 'Tonics'),
        ('Nature Made', 'Nature Made'),
        ('Enzymes', 'Enzymes'),
        ('Probiotics', 'Probiotics'),
        ('Adaptogens', 'Adaptogens'),
        ('Antioxidants', 'Antioxidants'),
    ]
    PharmacyGrouping = models.CharField(max_length=255, choices=NAME_CHOICES, unique=True)

    def __str__(self):
        return self.name


# 2. Brands
class Brand(models.Model):
    NAME_CHOICES = [
        ('Nature\'s Field', 'Nature\'s Field'),
        ('Puritan\'s Pride', 'Puritan\'s Pride'),
        ('Vitabiotics', 'Vitabiotics'),
        ('Centrum', 'Centrum'),
        ('Seven Seas', 'Seven Seas'),
        ('Reload', 'Reload'),
        ('Goli', 'Goli'),
        ('Olly', 'Olly'),
        ('Earth\'s Creation', 'Earth\'s Creation'),
        ('Piping Rock', 'Piping Rock'),
        ('Solgar', 'Solgar'),
        ('Country Life', 'Country Life'),
        ('Mason\'s Natural', 'Mason\'s Natural'),
        ('Garden of Life', 'Garden of Life'),
        ('Nature\'s Truth', 'Nature\'s Truth'),
        ('Swanson', 'Swanson'),
        ('Emzor', 'Emzor'),
        ('M&B', 'M&B'),
        ('Force Factor', 'Force Factor'),
        ('Renew Life', 'Renew Life'),
        ('Elbe', 'Elbe'),
        ('Relumins', 'Relumins'),
        ('Nutrify', 'Nutrify'),
        ('Mega We Care', 'Mega We Care'),
        ('Winstown', 'Winstown'),
        ('Optibac', 'Optibac'),
        ('Holand & Barett', 'Holand & Barett'),
        ('Horbach', 'Horbach'),
        ('Himalaya', 'Himalaya'),
        ('Nature\'s Bounty', 'Nature\'s Bounty'),
        ('Now', 'Now'),
        ('Organic Health', 'Organic Health'),
        ('Imedeen', 'Imedeen'),
        ('Renzo', 'Renzo'),
        ('Kirkland', 'Kirkland'),
        ('Haliborange', 'Haliborange'),
        ('Wholesome Foods', 'Wholesome Foods'),
        ('Max World', 'Max World'),
        ('Fafor Life', 'Fafor Life'),
        ('Super Life', 'Super Life'),
        ('Bayer', 'Bayer'),
        ('Dr. Meyer', 'Dr. Meyer'),
        ('Live Pure', 'Live Pure'),
        ('Gain World', 'Gain World'),
        ('21st Century', '21st Century'),
        ('Gaia', 'Gaia'),
        ('Doctor\'s Best', 'Doctor\'s Best'),
    ]
    Brand_Name = models.CharField(max_length=255, choices=NAME_CHOICES, unique=True)

    def __str__(self):
        return self.name


# 3. Age
class AgeGroup(models.Model):
    NAME_CHOICES = [
        ('70+', '60'),
        ('60+', '60+'),
        ('50+', '50+'),
        ('40+', '40+'),
        ('general','general'),
        ('Young Adults', 'Young Adults'),
        ('Adults', 'Adults'),
        ('Teens', 'Teens'),
        ('Children (General)', 'Children (General)'),
        ('Toddlers', 'Toddlers'),
        ('Infant', 'Infant')
    ]
    Age = models.CharField(max_length=255, choices=NAME_CHOICES, unique=True)

    def __str__(self):
        return self.name
    
class AgeRange(models.Model):
        name = models.CharField(max_length=255)
        min_age = models.IntegerField()
        max_age = models.IntegerField()



# 4. Gender
class Gender(models.Model):
    NAME_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('For Teen Girls', 'For Teen Girls'),
        ('For Teen Boys', 'For Teen Boys'),
        ('For Women', 'For Women'),
        ('For Men', 'For Men'),
    ]
    Gender = models.CharField(max_length=255, choices=NAME_CHOICES, unique=True)

    def __str__(self):
        return self.name


# 8. Lifestyle
class Lifestyle(models.Model):
    NAME_CHOICES = [
        ('For Sex Enthusiasts', 'For Sex Enthusiasts'),
        ('For Clubbers', 'For Clubbers'),
        ('For Smokers', 'For Smokers'),
        ('For Drinkers', 'For Drinkers'),
        ('Gym Enthusiasts', 'Gym Enthusiasts'),
        ('Skin and Fashion Lovers', 'Skin and Fashion Lovers'),
        ('Prayers and Spiritual Exercises (Meditation, Fasting, Yoga)', 'Prayers and Spiritual Exercises (Meditation, Fasting, Yoga)'),
    ]
    LifestyleType = models.CharField(max_length=255, choices=NAME_CHOICES, unique=True)

    def __str__(self):
        return self.name


# 10. Dosage Forms
class DosageForm(models.Model):
    NAME_CHOICES = [
        ('Creams', 'Creams'),
        ('Gummies', 'Gummies'),
        ('Inhalers', 'Inhalers'),
        ('Patches', 'Patches'),
        ('Liquid', 'Liquid'),
        ('Powders', 'Powders'),
        ('Capsules', 'Capsules'),
        ('Tablets', 'Tablets'),
    ]
    DosageForm = models.CharField(max_length=255, choices=NAME_CHOICES, unique=True)

    def __str__(self):
        return self.name


# 11. Lifestyle Rating
class LifestyleRating(models.Model):
    NAME_CHOICES = [
        ('Vitality', 'Vitality'),
        ('Immunity', 'Immunity'),
        ('Quick Recovery', 'Quick Recovery'),
        ('Brain Power (Wealth Creation)', 'Brain Power (Wealth Creation)'),
        ('Skin, Beauty, Graceful Ageing', 'Skin, Beauty, Graceful Ageing'),
        ('Longevity', 'Longevity'),
    ]
    LifestyleRating = models.CharField(max_length=255, choices=NAME_CHOICES, unique=True)

    def __str__(self):
        return self.name


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
    description = models.TextField()
    main_image = models.ImageField(upload_to='product_images/main')
    image_1 = models.ImageField(upload_to='product_images/secondary', blank=True, null=True)
    image_2 = models.ImageField(upload_to='product_images/secondary', blank=True, null=True)
    image_3 = models.ImageField(upload_to='product_images/secondary', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.name


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # rating = models.IntegerField(choices=[1, 2, 3, 4, 5])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} - {self.user.username}"


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