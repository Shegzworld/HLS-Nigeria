from django.contrib import admin
from .models import Product, Health_Benefits,Health_support,Fortify,Side_effects

# Define admin interface for Product model

class HealthSupportInline(admin.TabularInline):
    model = Health_Benefits
    extra = 1 

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_health_conditions')
    inlines = [HealthSupportInline]

    def get_health_conditions(self, obj):
        conditions = [hs.health_condition for hs in obj.health_support_set.all()]
        return ", ".join(conditions)

# Register other models with default admin interface
models = [ Health_support, Fortify, Side_effects, Health_Benefits]
for model in models:
    admin.site.register(model)