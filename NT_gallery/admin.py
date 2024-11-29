from django.contrib import admin
from .models import Product, Health_Benefits, Health_support, Fortify, Side_effects,ProductReview,ProductSubscription,LSV

# Define admin interface for Product model

class HealthSupportInline(admin.TabularInline):
    model = Health_Benefits
    extra = 1 



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category','price')
    inlines = [HealthSupportInline]
    filter_horizontal = ('lsvs',)  # Enable a multi-select widget for LSVs in the admin

    def get_lsvs(self, obj):
        return ", ".join([lsv.name for lsv in obj.lsvs.all()])

    get_lsvs.short_description = 'LSVs'

class StoreAdminArea(admin.AdminSite):
    site_header = 'HLS Store Portal'

store_site = StoreAdminArea(name = 'Store portal')

store_site.register(Product)
store_site.register(Health_Benefits)
store_site.register(Health_support)
store_site.register(Fortify)
store_site.register(Side_effects)
store_site.register(ProductReview)
store_site.register(ProductSubscription)

    # def get_health_conditions(self, obj):
    #     # Check if health_support is associated with this product
    #     if obj.health_support:
    #         return obj.health_support.health_condition
    #     return "No health support assigned"

    # def get_fortify(self, obj):
    #     # Check if fortify is associated with this product
    #     if obj.fortify:
    #         return obj.fortify.name
    #     return "No fortify assigned"

    # def get_side_effects(self, obj):
    #     # Check if side_effect is associated with this product
    #     if obj.side_effect:
    #         return obj.side_effect.medication
    #     return "No side effects assigned"

    # get_health_conditions.short_description = "Health Conditions"  # Optional: Set column header in admin display
    # get_fortify.short_description = "Fortify"
    # get_side_effects.short_description = "Side Effects"

# Register other models with default admin interface
models = [Health_support, Fortify, Side_effects, Health_Benefits,ProductReview,ProductSubscription]
for model in models:
    admin.site.register(model)
@admin.register(LSV)
class LSVAdmin(admin.ModelAdmin):
    list_display = ('name',)

