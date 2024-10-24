from django.contrib import admin
from .models import Product,PharmacyGrouping,AgeRange, Brand, Gender,Lifestyle, DosageForm, LifestyleRating,Health_Benefits,Health_support,Side_effects,Fortify


# Register your models here.

models = [Product, PharmacyGrouping, Brand,AgeRange, Gender,Lifestyle, DosageForm, LifestyleRating,Health_Benefits, Health_support, Side_effects, Fortify]

class Product(admin.ModelAdmin):
    inlines = [Product,PharmacyGrouping, Brand, AgeRange, Gender,Lifestyle, DosageForm, LifestyleRating,Health_Benefits, Health_support, Side_effects, Fortify]

for model in models:
    admin.site.register(model)


