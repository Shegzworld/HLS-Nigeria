from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    created_at = models.DateTimeField(default=now)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message[:30]}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # New field for budget
    new_notifications_count = models.IntegerField(default=0)  # Tracks unread notifications

    
    def __str__(self):
        return f"{self.user.username}"

class Basic(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='basics')
    nickname = models.CharField(max_length=255)
    age = models.CharField(max_length=255,null=True, blank=True)  # New field for age
    gender = models.CharField(max_length=255,null=True, blank=True)
    weight =models.CharField(max_length=255,null=True, blank=True) 
    height =models.CharField(max_length=255,null=True, blank=True) 

    def __str__(self):
        return f"{self.user_profile.user.username}'s Basic info"

class Lifestyle(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='lifestyle')
    habits = models.CharField(max_length=255, null=True, blank=True)
    recreation = models.CharField(max_length=255, null=True, blank=True)
    lifestyle = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.user_profile.user.username}'s Lifestyle info"

class HealthCondition(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='health_condition')
    health_complaints = models.CharField(max_length=255, null=True, blank=True)
    current_medications = models.CharField(max_length=255, null=True, blank=True)
    genetic_history = models.CharField(max_length=255, null=True, blank=True)
    allergies = models.CharField(max_length=255, null=True, blank=True)
    health_fears = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user_profile.user.username}'s Health Condition info"

class Preference(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='preferences')
    drug_form = models.CharField(max_length=20, null=True, blank=True)
    health_budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.user_profile.user.username}'s Preference info"





