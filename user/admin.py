from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from user.models import UserProfile, Basic, Lifestyle, HealthCondition, Preference

# Inline models for UserProfile and other models
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    extra = 1

class BasicInline(admin.StackedInline):
    model = Basic
    extra = 1

class LifestyleInline(admin.StackedInline):
    model = Lifestyle
    extra = 1

class HealthConditionInline(admin.StackedInline):
    model = HealthCondition
    extra = 1

class PreferenceInline(admin.StackedInline):
    model = Preference
    extra = 1

# UserProfileAdmin now inherits from InlineModelAdmin
class UserProfileAdmin(admin.ModelAdmin):
    inlines = [BasicInline, LifestyleInline, HealthConditionInline, PreferenceInline]

# Register the UserProfile model and its inlines
admin.site.register(UserProfile, UserProfileAdmin)

# Add UserProfileInline to the UserAdmin
UserAdmin.inlines = [UserProfileInline]
admin.site.unregister(User)  # Unregister the default UserAdmin to register a customized one
admin.site.register(User, UserAdmin)  # Register the customized UserAdmin
