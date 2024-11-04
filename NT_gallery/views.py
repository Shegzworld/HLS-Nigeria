from django.shortcuts import render
from .models import Profile, Product

def ntg_view(request):
    profile = Profile.objects.get(user=request.user)
    relevant_products = Product.objects.filter(
        suitable_for__in=profile.medical_conditions.all(),
        addresses__in=profile.health_goals.all(),
        lifestyle_compatibility__in=profile.lifestyle.all(),
        price__lte=profile.budget
    )
    return render(request, 'dashboard/NT_gallery.html', {'products': relevant_products})
