from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username}"


class Basic(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='basics')
    nickname = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    age = models.IntegerField(null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return f"{self.user_profile.user.username}{"'s"}-{"Basic info"}"
    


class Lifestyle(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='lifestyle')
    habits = models.CharField(max_length=255, null=True, blank=True)
    recreation = models.CharField(max_length=255, null=True, blank=True)
    lifestyle = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.user_profile.user.username}-{"Basic info"}"


class HealthCondition(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='health')
    health_complaints = models.CharField(max_length=255, null=True, blank=True)
    current_medications = models.CharField(max_length=255, null=True, blank=True)
    genetic_history = models.CharField(max_length=255, null=True, blank=True)
    allergies = models.CharField(max_length=255, null=True, blank=True)
    health_fears = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user_profile.user.username}-{"HealthCondition info"}"


class Preference(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='preference')
    drug_form = models.CharField(max_length=20, null=True, blank=True)
    health_budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.user_profile.user.username}-{"Preference info"}"



