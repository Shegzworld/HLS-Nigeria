from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import UserProfile
from .forms import UserRegistrationForm,CustomLoginForm,BasicsForm,HealthConditionForm,PreferenceForm,LifestyleForm
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from NT_gallery.models import ProductReview, ProductSubscription

def register_view(request):
    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)
        basics = request.session.get('basics')
        lifestyle = request.session.get('lifestyle')
        health_condition = request.session.get('health_condition')
        preference = request.session.get('preference')
        print(request.session)
        if registration_form.is_valid():
            user = registration_form.save()
            UserProfile.objects.create(user=user)

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

            # Add a success message to notify the user
            messages.success(request, "Your account has been created successfully! You can now log in.")
            return redirect('user:login')
        else:
            # Add an error message if the form is invalid
            messages.error(request, "There was an error with your registration. Please try again.")
    else:
        registration_form = UserRegistrationForm()

    return render(request, 'user/register.html', {'registration_form': registration_form})


def login_view(request):
    if request.method == "POST":
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, "You have logged in successfully!")
            return redirect("dashboard:dashboard")
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    else:
        form = CustomLoginForm()

    return render(request, "user/login.html", {"form": form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "You have logged out successfully!")
        return redirect("home:homepage")
    

@receiver(post_save, sender=ProductReview)
def send_review_notification(sender, instance, created, **kwargs):
    if created:  # Only send notifications when a new review is created
        product = instance.product  # Get the product being reviewed
        subscriptions = ProductSubscription.objects.filter(product=product)  # Get all subscriptions for the product
        
        # Collect the email addresses of all users subscribed to this product
        subscriber_emails = [sub.user.email for sub in subscriptions]
        
        if subscriber_emails:
            subject = f"New Review on {product.name}"
            message = f"A new review has been posted for {product.name}:\n\n{instance.comment}\n\nCheck it out!"
            
            # Send email to all subscribed users
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,  
                subscriber_emails,
                fail_silently=False,
            )
