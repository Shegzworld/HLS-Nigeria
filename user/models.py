# from django.db import models
# from django.contrib.auth.models import User

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
#     profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
#     bio = models.TextField(null=True, blank=True)
#     budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # New field for budget
#     health_condition = models.CharField(max_length=255, null=True, blank=True)  # Add health_condition field
#     lifestyle = models.CharField(max_length=255, null=True, blank=True)  # Add lifestyle field
#     age = models.PositiveIntegerField(null=True, blank=True)  # New field for age

#     def __str__(self):
#         return f"{self.user.username}"

# class Basic(models.Model):
#     user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='basics')
#     nickname = models.CharField(max_length=255)
#     gender = models.CharField(max_length=10)
#     age = models.IntegerField(null=True, blank=True)
#     weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
#     height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

#     def __str__(self):
#         return f"{self.user_profile.user.username}'s Basic info"

# class Lifestyle(models.Model):
#     user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='lifestyle')
#     habits = models.CharField(max_length=255, null=True, blank=True)
#     recreation = models.CharField(max_length=255, null=True, blank=True)
#     lifestyle = models.CharField(max_length=255, null=True, blank=True)

#     def __str__(self):
#         return f"{self.user_profile.user.username}'s Lifestyle info"

# class HealthCondition(models.Model):
#     user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='health_condition')
#     health_complaints = models.CharField(max_length=255, null=True, blank=True)
#     current_medications = models.CharField(max_length=255, null=True, blank=True)
#     genetic_history = models.CharField(max_length=255, null=True, blank=True)
#     allergies = models.CharField(max_length=255, null=True, blank=True)
#     health_fears = models.TextField(null=True, blank=True)

#     def __str__(self):
#         return f"{self.user_profile.user.username}'s Health Condition info"

# class Preference(models.Model):
#     user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='preferences')
#     drug_form = models.CharField(max_length=20, null=True, blank=True)
#     health_budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

#     def __str__(self):
#         return f"{self.user_profile.user.username}'s Preference info"


from django.db import models
from django.contrib.auth.models import User


# all field has been added to userprofile to aviod redundancy
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Budget for health
    health_condition = models.CharField(max_length=255, null=True, blank=True)  # Health condition
    lifestyle = models.CharField(max_length=255, null=True, blank=True)  # Lifestyle habits
    age = models.PositiveIntegerField(null=True, blank=True)  # User age
    nickname = models.CharField(max_length=255, null=True, blank=True)  # Basic info - nickname
    gender = models.CharField(max_length=10, null=True, blank=True)  # Gender
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Weight
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Height
    habits = models.CharField(max_length=255, null=True, blank=True)  # Lifestyle habits
    recreation = models.CharField(max_length=255, null=True, blank=True)  # Recreational activities
    health_complaints = models.CharField(max_length=255, null=True, blank=True)  # Health complaints
    current_medications = models.CharField(max_length=255, null=True, blank=True)  # Current medications
    genetic_history = models.CharField(max_length=255, null=True, blank=True)  # Genetic history
    allergies = models.CharField(max_length=255, null=True, blank=True)  # Allergies
    health_fears = models.TextField(null=True, blank=True)  # Health-related fears
    drug_form = models.CharField(max_length=20, null=True, blank=True)  # Preference for drug form
    health_budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Budget for health-related preferences

    def __str__(self):
        return f"{self.user.username}"

