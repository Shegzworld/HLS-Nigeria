from django.contrib import admin
from .models import Product,PharmacyGrouping, Brand, AgeGroup, Gender,Lifestyle, DosageForm, LifestyleRating


# Register your models here.

models = [Product, PharmacyGrouping, Brand, AgeGroup, Gender,Lifestyle, DosageForm, LifestyleRating]

for model in models:
    admin.site.register(model)
# admin.site.register(Product)
# admin.site.register(PharmacyGrouping)
# admin.site.register(Brand)
# admin.site.register(AgeGroup)
# admin.site.register(Gender)
# admin.site.register(Lifestyle)
# admin.site.register(DosageForm)
# admin.site.register(LifestyleRating)

