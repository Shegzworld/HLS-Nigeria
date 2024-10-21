from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from django.contrib import messages
from .models import UserProfile
from .forms import UserRegistrationForm, BasicsForm, LifestyleForm, HealthConditionForm, PreferenceForm, CustomLoginForm


def register_view(request):
    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)
        basics = request.session.get('basics')
        lifestyle = request.session.get('lifestyle')
        health_condition = request.session.get('health_condition')
        preference = request.session.get('preference')

        if registration_form.is_valid():
            user = registration_form.save()
            UserProfile.objects.create(user=user)
            # messages.success(request, "Account created, you now have a dashboard")

            # Save form data to corresponding models
            if basics:
                basics = BasicsForm(basics).save(commit=False)
                basics.user_profile = user.profile
                basics.save()
            
            if lifestyle:
                lifestyle = LifestyleForm(lifestyle).save(commit=False)
                lifestyle.user_profile = user.profile
                lifestyle.save()

            if health_condition:
                health_condition = HealthConditionForm(health_condition).save(commit=False)
                health_condition.user_profile = user.profile
                health_condition.save()

            if preference:
                preference = PreferenceForm(preference).save(commit=False)
                preference.user_profile = user.profile
                preference.save()

            # login(request, user)
            return redirect('user:login')
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'user/register.html', {'registration_form': registration_form})


def login_view(request):
    if request.method == "POST":
        form = CustomLoginForm(data = request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("dashboard:dashboard")
    else:
        form = CustomLoginForm()
    return render(request, "user/login.html", {"form":form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("home:homepage")