# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('new', views.create_product, name='create_product'),
]