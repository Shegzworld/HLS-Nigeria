from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from blog.models import Blog
from user.models import UserProfile,Basic, Lifestyle, Preference
from NT_gallery.models import Product
from podcasts.models import Podcast,Episode
from django.core.paginator import Paginator
from django.db.models import Count,Subquery,OuterRef,Q
from django.core.paginator import Paginator

class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    #     # fetch user and and instantiate userprofiles and subprofiles
    #     user = self.request.user
    #     user_profile = UserProfile.objects.get(user=user)
    #     print(user_profile)

    #     basic = Basic.objects.get(user_profile=user_profile)
    #     lifestyle = Lifestyle.objects.get(user_profile=user_profile)
    #     preference = Preference.objects.get(user_profile=user_profile)



    #     # Product filtering by Basics(age and gender)
    #     products_by_age = Product.objects.filter(
    #         Q(age_range__min_age__lte=basic.age, age_range__max_age__gte=basic.age) | 
    #         Q(age_range__name=basic.age) | 
    #         Q(age_range__name='General')
    #     )

    #     products_by_gender = Product.objects.filter(
    #         Q(gender__exact=basic.gender) | 
    #         Q(gender__exact='Unisex') | 
    #         Q(gender__isnull=True)
    #     )

    # # Product filtering by Lifestyle(habits, recreation,lifestyle)
    #     products_by_lifestyle = Product.objects.filter(
    #         Q(lifestyle__icontains=lifestyle.habits) | 
    #         Q(lifestyle__icontains=lifestyle.recreation) | 
    #         Q(lifestyle__icontains=lifestyle.lifestyle)
    #     ).distinct()



    #     # Product filtering by Preferences(drug form, and budget)
    #     preferred_dosage_forms = preference.drug_form.split(',')
    #     preferred_dosage_forms = [drug_form.strip() for drug_form in preferred_dosage_forms]
    #     products_by_drugForm = Product.objects.filter(
    #     Q(dosage_form__in=preferred_dosage_forms)
    #     )

    #     products_by_budget = Product.objects.filter(
    #     Q(price__lte=preference.health_budget)
    #     )

        
    #     # Combining all filtered products
    #     products = products_by_age & products_by_gender & products_by_drugForm & products_by_budget & products_by_lifestyle

    #     paginator = Paginator(products, 9) 
    #     page_number = self.request.GET.get('page')
    #     products = paginator.get_page(page_number)


        blog_list = Blog.objects.all()
        
        podcast_list = Podcast.objects.annotate(episode_count=Count('episodes'))
        podcast_list = Podcast.objects.all()
        paginator = Paginator(podcast_list, 5)
        page_number = self.request.GET.get('page')
        podcast_page = paginator.get_page(page_number)
        
        context['blog_list'] = blog_list
        # context['product_list'] = products
        context['podcast_list'] = podcast_page
        
        return context

    