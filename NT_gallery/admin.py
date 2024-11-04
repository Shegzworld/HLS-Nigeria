from django.contrib import admin
from .models import Product, PharmacyGrouping, Brand, AgeRange, Gender, Lifestyle, DosageForm, Health_Benefits, Health_support, Side_effects, Fortify, ProductReview

# Define admin interface for Product model

class HealthSupportInline(admin.TabularInline):
    model = Health_support
    extra = 1 

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_health_conditions')
    inlines = [HealthSupportInline]

    def get_health_conditions(self, obj):
        conditions = [hs.health_condition for hs in obj.health_support_set.all()]
        return ", ".join(conditions)

# Register other models with default admin interface
models = [PharmacyGrouping, Brand, AgeRange, Gender, Lifestyle, DosageForm, Health_Benefits, Health_support, Side_effects, Fortify, ProductReview]
for model in models:
    admin.site.register(model)