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
from user.models import Notification,HealthCondition,Lifestyle,Basic

class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = self.get_user_profile()
        products = self.filter_products(user_profile)

        print(products)
        # products_by_attribute = self.group_products(products)
        # packs = self.assign_products_to_packs(products_by_attribute)
        # context['specifics'] = products_by_attribute
        # context['nutrient_gallery'] = packs
        
        blog_list = Blog.objects.all()
        blog_paginator = Paginator(blog_list, 5)
        blog_page_number = self.request.GET.get('page', 1)
        blog_page = blog_paginator.get_page(blog_page_number)
        context['blog_list'] = blog_page
        
        
        podcast_list = Podcast.objects.annotate(episode_count=Count('episodes'))
        podcast_paginator = Paginator(podcast_list, 5)
        podcast_page_number = self.request.GET.get('page', 1)
        podcast_page = podcast_paginator.get_page(podcast_page_number)
        context['podcast_list'] = podcast_page

         # Notification count for the logged-in user
        user = self.request.user
        notification_count = Notification.objects.filter(
            user=user,
            is_read=False  # Example condition, adjust based on your notification model
        ).count()

        # Add to context if the count > 0
        if notification_count > 0:
            context['notification_count'] = notification_count
        else:
            context['notification_count'] = None
        
        return context

    def get_user_profile(self):
        user = self.request.user
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        if created:
            messages.info(self.request, "Your user profile was automatically created.")
        return user_profile

    def filter_products(self, user_profile):
        user_health = HealthCondition.objects.filter(
            user_profile=user_profile)
        user_basic = Basic.objects.filter(
            user_profile=user_profile)
        user_lifestyle = Lifestyle.objects.filter(
            user_profile=user_profile)
        products_with_health_benefits = Product.objects.filter(
                # Q(health_benefit__fortify__in=[some_fortify_value]) |  
                Q(health_benefit__health_support__health_condition__in=user_health.values('condition_as_str'))
         ).select_related('health_benefit').prefetch_related('health_benefit__fortify', 'health_benefit__health_support')
        
        return products_with_health_benefits


    def group_products(self, products):
        products_by_attribute = {}
        for product in products:
            attribute = product.health_condition or product.fortify or product.basics.age or product.basics.gender
            if attribute not in products_by_attribute:
                products_by_attribute[attribute] = []
            products_by_attribute[attribute].append(product)
        return products_by_attribute

    def assign_products_to_packs(self, products_by_attribute,user_profile):
        budget = user_profile.budget or 0
        packs = [
            {'name': 'Pro Pack', 'min_price': budget, 'max_price': budget * 1.4},
            {'name': 'Dr Pack', 'min_price': budget, 'max_price': budget * 1.2},
            {'name': 'Economy Pack', 'min_price': budget, 'max_price': budget * 1.05},
            {'name': 'Welfare Pack', 'min_price': budget * 0.9, 'max_price': budget}
        ]
        packs = [{**pack, 'products': []} for pack in packs]
        for attribute, products in products_by_attribute.items():
            for pack in packs:
                if len(pack['products']) < 3:
                    for product in products:
                        if pack['min_price'] <= product.price <= pack['max_price']:
                            pack['products'].append(product)
                            pack['total_price'] = sum(p.price for p in pack['products'])
                            break
                    break
        self.adjust_pack_prices(packs)
        return packs

    def adjust_pack_prices(self, packs):
        for pack in packs:
            if pack['total_price'] > pack['max_price'] and len(pack['products']) < 3:
                self.adjust_price(pack)
    
    def adjust_price(self, pack,products_by_attribute):
        cheapest_product = min(pack['products'], key=lambda x: x.price)
        pack['products'].remove(cheapest_product)
        pack['total_price'] -= cheapest_product.price
        # Reassign cheapest product to another attribute
        for attribute, products in products_by_attribute.items():
            if attribute != cheapest_product.health_condition and attribute != cheapest_product.fortify:
                products.append(cheapest_product)
                for product in products:
                    if product.price <= pack['max_price'] - pack['total_price']:
                        pack['products'].append(product)
                        pack['total_price'] += product.price
                        break
                else:
                    lowest_priced = min(products, key=lambda x: x.price)
                    pack['products'].append(lowest_priced)
                    pack['total_price'] += lowest_priced.price
                break
        
        
class Blog_detail(DetailView):
    model = Blog
    template_name = 'dashboard/blog_detail.html'
    context_object_name = 'post'
    
