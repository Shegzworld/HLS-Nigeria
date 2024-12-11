from django.urls import path
from .views import Dashboard
from .views import Blog_detail
from .views import product_detail

app_name = 'dashboard'

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('blog/<int:pk>/', Blog_detail.as_view(), name='blog_detail'),
    path('dr_picks/<int:pk>/', product_detail, name='product_info'),
]
