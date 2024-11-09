from django.contrib import admin
from .models import Products, Health_Benefits,Category,SubCategory,MainCategory,DetoxOption,HealthSupportOption,FortifyOption,ProductReview

# Define admin interface for Product model

class HealthSupportInline(admin.TabularInline):
    model = Health_Benefits
    extra = 1 

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_health_conditions')
    inlines = [HealthSupportInline]

    def get_health_conditions(self, obj):
        conditions = [hs.health_condition for hs in obj.health_support_set.all()]
        return ", ".join(conditions)

# Register other models with default admin interface
models = [Category, SubCategory, MainCategory, DetoxOption, HealthSupportOption, FortifyOption, Health_Benefits, ProductReview]
for model in models:
    admin.site.register(model)