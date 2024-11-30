from django.urls import path
from .views import homepage
from .import views

app_name = 'home'

urlpatterns = [
    path('', homepage, name = "homepage"),
    path('quiz/', views.quiz_page, name = "quiz")
]
