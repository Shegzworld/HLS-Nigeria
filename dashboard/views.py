from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView,DetailView
from blog.models import Blog
from user.models import UserProfile
from podcasts.models import Podcast,Episode
from decimal import Decimal
from django.core.paginator import Paginator
from django.db.models import Count,Subquery,OuterRef,Q
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from NT_gallery.models import Product
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib import messages
from user.models import HealthCondition,Lifestyle,Basic
# from user.models import Notification
import boto3
import os

class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # user_p
        # profile = self.get_user_profile()
        # products = self.filter_products(user_profile)

        # print(products)
        # products_by_attribute = self.group_products(products)
        # packs = self.assign_products_to_packs(products_by_attribute)
        # context['specifics'] = products_by_attribute
        # context['nutrient_gallery'] = packs


        
            #     products = Product.objects.filter(
            #     Q(sub_categories__gender_icontains="female") |  
            #     Q(sub_categories__age__icontains="teen")         
            # )
        unique_products = Product.objects.all()

        # Initialize empty lists to store products
        products_with_images = []
        products_with_missing_images = []

        # Get the list of image keys from S3
        s3 = boto3.client('s3', aws_access_key_id='AKIATFBMO53EKIXSNNUY',aws_secret_access_key='vf+xxthS0G7T4l37rtvmYdzhiR4yEZQS3yXHIfsz')
        image_keys = []
        bucket_name = 'hlsnigeriabucket'  # Replace with your actual bucket name
        prefix = 'product_image'
        kwargs = {'Bucket': bucket_name, 'Prefix': prefix}

        while True:
            response = s3.list_objects_v2(**kwargs)
            image_keys.extend([obj['Key'] for obj in response.get('Contents', [])])

            try:
                kwargs['ContinuationToken'] = response['NextContinuationToken']
            except KeyError:
                break

        for product in unique_products:
            if product.main_image in image_keys:
                # If image exists, add product to products_with_images
                products_with_images.append(product)
            else:
                # If image is missing, add product to products_with_missing_images
                products_with_missing_images.append(product)

        # Combine the two lists, with products with missing images at the end
        final_product_list = products_with_images + products_with_missing_images
        # Paginate the final product list
        paginator = Paginator(final_product_list, 10)  # Show 10 products per page
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # Return the paginated products
        context['dr_picks'] = page_obj
        
        blog_list = Blog.objects.all().order_by('-created_at') #Blog.objects.all()
        blog_paginator = Paginator(blog_list, 10)
        blog_page_number = self.request.GET.get('page')
        blog_page = blog_paginator.get_page(blog_page_number)
        context['blog_list'] = blog_page
        
        
        podcast_list = Podcast.objects.annotate(episode_count=Count('episodes'))
        podcast_paginator = Paginator(podcast_list, 10)
        podcast_page_number = self.request.GET.get('page')
        podcast_page = podcast_paginator.get_page(podcast_page_number)
        context['podcast_list'] = podcast_page

         # Notification count for the logged-in user
        # user = self.request.user
        # notification_count = Notification.objects.filter(
        #     user=user,
        #     is_read=False  # Example condition, adjust based on your notification model
        # ).count()

        # # Add to context if the count > 0
        # if notification_count > 0:
        #     context['notification_count'] = notification_count
        # else:
        #     context['notification_count'] = None
        
        return context
    def get(self, request, *args, **kwargs):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            # Handle AJAX request
            context = self.get_context_data(**kwargs)
            html = render_to_string('dashboard/partials/paginated_content.html', context)
            return JsonResponse({'html': html})
        else:
            # Handle normal request
            return super().get(request, *args, **kwargs)
        
    def get_user_profile(self):
        user = self.request.user
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        if created:
            messages.info(self.request, "Your user profile was automatically created. complete quiz to get your personal nutrient type gallery")
        return user_profile

    def filter_products(self, user_profile):
        user_health = HealthCondition.objects.filter(
            user_profile=user_profile)
        user_basic = Basic.objects.filter(
            user_profile=user_profile)
        # print(user_health)
        user_lifestyle = Lifestyle.objects.filter(
            user_profile=user_profile)
        # return Product.objects.all()
       # products_with_health_benefits = Product.objects.filter(
              #  Q(health_benefit.fortify.organ==user_profile.lifestyle.habit))
        #.select_related('health_benefit.fortify.organ')
                #  Q(health_benefit__health_support__health_condition__in=user_health)
         #).select_related('health_benefit').prefetch_related('health_benefit__fortify', 'health_benefit__health_support')
        
        # return products_with_health_benefits

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
    

def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'dashboard/product_info.html', {'product':product})
