# from django.db import models
# from django.contrib.auth.models import User


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null = True)
#     profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
#     bio = models.TextField(null=True, blank=True)
    
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
#         return f"{self.user_profile.user.username}{"'s"}-{"Basic info"}"
    


# class Lifestyle(models.Model):
#     user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='lifestyle')
#     habits = models.CharField(max_length=255, null=True, blank=True)
#     recreation = models.CharField(max_length=255, null=True, blank=True)
#     lifestyle = models.CharField(max_length=255, null=True, blank=True)

#     def __str__(self):
#         return f"{self.user_profile.user.username}-{"Basic info"}"


# class HealthCondition(models.Model):
#     user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='health')
#     health_complaints = models.CharField(max_length=255, null=True, blank=True)
#     current_medications = models.CharField(max_length=255, null=True, blank=True)
#     genetic_history = models.CharField(max_length=255, null=True, blank=True)
#     allergies = models.CharField(max_length=255, null=True, blank=True)
#     health_fears = models.TextField(null=True, blank=True)

#     def __str__(self):
#         return f"{self.user_profile.user.username}-{"HealthCondition info"}"


# class Preference(models.Model):
#     user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='preference')
#     drug_form = models.CharField(max_length=20, null=True, blank=True)
#     health_budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

#     def __str__(self):
#         return f"{self.user_profile.user.username}-{"Preference info"}"



from django.db import models
from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser, BaseUserManager

# Custom User Manager to handle user creation
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('The Email field is required')
        if not username:
            raise ValueError('The Username field is required')
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email=email,
            username=username,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db) 
        return user

# Custom User Model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.email

    # Override groups and user_permissions fields inherited from PermissionsMixin to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Use a custom related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',  # Use a custom related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

# Abstract class for UserProfile Information
class AbstractUserProfile(models.Model):
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.user.username}'s Profile"

# Extend AbstractUserProfile for Basic Info
class BasicInfo(AbstractUserProfile):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='basic_info')
    nickname = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    age = models.IntegerField(null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - Basic Info"

# Extend AbstractUserProfile for Lifestyle Info
class LifestyleInfo(AbstractUserProfile):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='lifestyle_info')
    habits = models.CharField(max_length=255, null=True, blank=True)
    recreation = models.CharField(max_length=255, null=True, blank=True)
    lifestyle = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - Lifestyle Info"

# Extend AbstractUserProfile for Health Conditions
class HealthConditionInfo(AbstractUserProfile):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='health_condition')
    health_complaints = models.CharField(max_length=255, null=True, blank=True)
    current_medications = models.CharField(max_length=255, null=True, blank=True)
    genetic_history = models.CharField(max_length=255, null=True, blank=True)
    allergies = models.CharField(max_length=255, null=True, blank=True)
    health_fears = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - Health Condition Info"

# Extend AbstractUserProfile for Preferences
class PreferenceInfo(AbstractUserProfile):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='preference_info')
    drug_form = models.CharField(max_length=20, null=True, blank=True)
    health_budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - Preference Info"
