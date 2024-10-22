from django.contrib import admin
from .models import CustomUser as UserProfile,BasicInfo as Basic,LifestyleInfo as Lifestyle,PreferenceInfo as Preference, HealthConditionInfo as HealthCondition
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

# class CustomUserAdmin(UserAdmin):
#     inlines = [BasicInline, LifestyleInline, HealthConditionInline, PreferenceInline]

class CustomUserAdmin(UserAdmin):
    model = UserProfile
    list_display = ['email', 'username', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ['email', 'username']
    ordering = ['email']
    filter_horizontal = ['groups', 'user_permissions']


# Register your models here.

# UserAdmin.inlines = [UserProfileInline]
admin.site.register(UserProfile,CustomUserAdmin)
# admin.site.register(Basic)
# admin.site.register(Lifestyle)
# admin.site.register(Preference)
# admin.site.register(HealthCondition)