from django.shortcuts import render
from .models import Product
# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from .models import Product
from .models import LSV, Flag_condition

@csrf_exempt  # Disable CSRF for this endpoint, optional for testing
# @require_POST
def create_product(request):
    print()
    if(request.method == "GET"):
         render(request, 'NT_gallery/dist/index.html')

    try:
        # Parse the JSON data from the request
        data = json.loads(request.body)
        
        # Create a new product instance and save it to the database
        product = Product(
            name=data.get('name'),
            category=data.get('category', ''),
            sub_categories=data.get('sub_categories', []),
            lsvs=data.get('lsvs', []),
            price=data.get('price'),
            strength=data.get('strength', ''),
            description=data.get('description', ''),
            pictures=data.get('pictures', {}),
            # fortify=data.get('fortify_id'),  # Assuming foreign key IDs are provided
            # side_effect=data.get('side_effect_id'),
            # health_support=data.get('health_support_id'),
            # author_id=data.get('author_id')  # Assuming the author ID is provided
        )
        
        # Save the product to the database
        product.save()

        # Return a success response
        # return render(request, 'dashboard/NT_gallery.html', {'products': relevant_products})
    
    except Exception as e:
        # Handle any errors and return an error response
        return JsonResponse({'error': 'Failed to create product', 'details': str(e)}, status=400)


# def ntg_view(request):
#     profile = Profile.objects.get(user=request.user)
#     relevant_products = Product.objects.filter(
#         suitable_for__in=profile.medical_conditions.all(),
#         addresses__in=profile.health_goals.all(),
#         lifestyle_compatibility__in=profile.lifestyle.all(),
#         price__lte=profile.budget
#     )
#     return render(request, 'dashboard/NT_gallery.html', {'products': relevant_products})
