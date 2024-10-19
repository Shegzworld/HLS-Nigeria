from django.contrib import admin
from .models import UserProfile,Basic,Lifestyle,Preference, HealthCondition
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


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

class UserProfileAdmin(admin.ModelAdmin):
    inlines = [BasicInline, LifestyleInline, HealthConditionInline, PreferenceInline]



# Register your models here.

UserAdmin.inlines = [UserProfileInline]
admin.site.register(UserProfile,UserProfileAdmin)
# admin.site.register(Basic)
# admin.site.register(Lifestyle)
# admin.site.register(Preference)
# admin.site.register(HealthCondition)