from django.urls import path
from .views import register_view,login_view,logout_view,beneficiary_list, beneficiary_detail, principal_list, principal_detail

app_name = 'user'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
     path('logout/', logout_view, name='logout'),
     path('beneficiaries/', beneficiary_list, name='beneficiary-list'),
    path('beneficiaries/<int:pk>/', beneficiary_detail, name='beneficiary-detail'),
    path('principals/', principal_list, name='principal-list'),
    path('principals/<int:pk>/', principal_detail, name='principal-detail'),

]
