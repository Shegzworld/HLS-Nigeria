from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import UserProfile
from .forms import UserRegistrationForm,CustomLoginForm,BasicsForm,HealthConditionForm,PreferenceForm,LifestyleForm
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Benfek, Principal
from .serializers import BenfekSerializer, PrincipalSerializer
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def beneficiary_list(request):
    if request.method == 'GET':
        # Allow a principal to only see their beneficiaries
        principal_id = request.user.id
        beneficiaries = Benfek.objects.filter(principal_id=principal_id)
        serializer = BenfekSerializer(beneficiaries, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        # Attach the principal ID to the request data
        data['principal'] = request.user.id
        serializer = BenfekSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def beneficiary_detail(request, pk):
    try:
        beneficiary = Benfek.objects.get(pk=pk, principal_id=request.user.id)
    except Benfek.DoesNotExist:
        return Response({'error': 'Beneficiary not found or not authorized'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BenfekSerializer(beneficiary)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BenfekSerializer(beneficiary, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        beneficiary.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def principal_list(request):
    if request.method == 'GET':
        principals = Principal.objects.all()
        serializer = PrincipalSerializer(principals, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PrincipalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def principal_detail(request, pk):
    try:
        principal = Principal.objects.get(pk=pk)
    except Principal.DoesNotExist:
        return Response({'error': 'Principal not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PrincipalSerializer(principal)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PrincipalSerializer(principal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        principal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)
        basics = request.session.get('basics')
        lifestyle = request.session.get('lifestyle')
        health_condition = request.session.get('health_condition')
        preference = request.session.get('preference')
        # print(basics)
        if registration_form.is_valid():
            user = registration_form.save()
            UserProfile.objects.create(user=user)
            # print(user.profile)
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

@csrf_exempt
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

@csrf_exempt
def logout_view(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "You have logged out successfully!")
        return redirect("home:homepage")
    

@login_required
def inbox_view(request):
    # Get the user's notifications
    notifications = request.user.notifications.order_by('-created_at')

    # Reset the new notifications count
    user_profile = request.user.profile
    user_profile.new_notifications_count = 0
    user_profile.save()

    # Mark notifications as read
    notifications.update(is_read=True)

    return render(request, 'inbox.html', {'notifications': notifications})