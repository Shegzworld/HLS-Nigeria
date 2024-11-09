from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView,DetailView
from blog.models import Blog
from user.models import UserProfile
# from NT_gallery.models import Product
from podcasts.models import Podcast,Episode
from decimal import Decimal
from django.core.paginator import Paginator
from django.db.models import Count,Subquery,OuterRef,Q
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from NT_gallery.models import Product
from django.contrib import messages

class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        # Use get_or_create to avoid DoesNotExist error
        user_profile, created = UserProfile.objects.get_or_create(user=user)

        # If the profile was just created, handle this case (optional)
        if created:
            
            messages.info(self.request, "Your user profile was automatically created.")

        # Define pack price tag ranges based on user's budget
        budget = user_profile.budget if user_profile.budget else 0  # Ensure budget is defined
        packs = [
    {'name': 'Pro Pack', 'min_price': budget, 'max_price': budget * Decimal('1.4')},  # Convert 1.4 to Decimal
    {'name': 'Dr Pack', 'min_price': budget, 'max_price': budget * Decimal('1.2')},   # Convert 1.2 to Decimal
    {'name': 'Economy Pack', 'min_price': budget, 'max_price': budget * Decimal('1.05')},  # Convert 1.05 to Decimal
    {'name': 'Welfare Pack', 'min_price': budget * Decimal('0.9'), 'max_price': budget}  # Convert 0.9 to Decimal
]

        # Filter  based on user's profile data
        products = Product.objects.filter(
            # Q(health_condition=user_profile.health_condition) |
            # Q(fortify=user_profile.lifestyle) |
            # Q(basics__age=user_profile.age, basics__gender=user_profile.gender)
        )

        # Group products by attribute
        products_by_attribute = {}
        for product in products:
            attribute = product.health_condition or product.fortify or product.basics.age or product.basics.gender
            if attribute not in products_by_attribute:
                products_by_attribute[attribute] = []
            products_by_attribute[attribute].append(product)

        # Initialize packs with empty product lists
        packs = [{**pack, 'products': []} for pack in packs]

        # Assign products to packs
        for attribute, products in products_by_attribute.items():
            for pack in packs:
                if len(pack['products']) < 3:
                    for product in products:
                        if pack['min_price'] <= product.price <= pack['max_price']:
                            pack['products'].append(product)
                            pack['total_price'] = sum(p.price for p in pack['products'])
                            break
                    break

        context['packs'] = packs

        # Blog and Podcast data
        blog_list = Blog.objects.all()
        podcast_list = Podcast.objects.annotate(episode_count=Count('episodes'))
        paginator = Paginator(podcast_list, 5)
        page_number = self.request.GET.get('page')
        podcast_page = paginator.get_page(page_number)
        
        context['blog_list'] = blog_list
        context['podcast_list'] = podcast_page
        
        return context
        
class Blog_detail(DetailView):
    model = Blog
    template_name = 'dashboard/blog_detail.html'
    context_object_name = 'post'
    