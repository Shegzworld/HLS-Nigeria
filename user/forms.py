from django import forms
from django.forms import Textarea
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import BasicInfo as Basic,LifestyleInfo as Lifestyle,PreferenceInfo as Preference, HealthConditionInfo as HealthCondition


# choices for all quiz classes

AGE_CHOICES = [
    ('Infant', 'Infant'),
    ('Toddlers', 'Toddlers'),
    ('Children (2-9)', 'Children (2-9)'),
    ('Teens', 'Teens'),
    ('Young Adults', 'Young Adults'),
    ('Adults', 'Adults'),
    ('40+', '40+'),
    ('50+', '50+'),
    ('60+', '60+'),
    ('70+', '70+'),
    ('general', 'general')
]

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
]

HABIT_CHOICES = [
    ('Smoking', 'Smoking'),
    ('Drinking', 'Drinking'),
    ('Sexing', 'Sexing'),
]

RECREATION_CHOICES = [
    ('Sport', 'Sport'),
    ('Board/Mind Games', 'Board/Mind Games'),
    ('Sexual Exercise', 'Sexual Exercise'),
    ('Fasting', 'Fasting'),
    ('Clubbing', 'Clubbing'),
    ('Dancing', 'Dancing'),
]

LIFESTYLE_CHOICES = [
    ('Skin Care', 'Skin Care'),
    ('Weight Management', 'Weight Management'),
    ('Energy cultivation', 'Energy cultivation'),
    ('Sleep Management', 'Sleep Management'),
    ('Sex Enhancement', 'Sex Enhancement'),
]

HEALTH_COMPLAINT_CHOICES = [
    ('Alzheimer', 'Alzheimer'),
    ('Arthritis', 'Arthritis'),
    ('Parkinson’s Disorder', 'Parkinson’s Disorder'),
    # Add more choices as needed
]

GENETIC_HISTORY_CHOICES = [
    ('Diabetes', 'Diabetes'),
    ('Hypertension', 'Hypertension'),
    ('Heart Disease', 'Heart Disease'),
    # Add more choices as needed
]

ALLERGY_CHOICES = [
    ('Drug Allergies', 'Drug Allergies'),
    ('Skin Allergies', 'Skin Allergies'),
    ('Food Allergies', 'Food Allergies'),
    ('Pet Allergies', 'Pet Allergies'),
    ('Dust Allergies', 'Dust Allergies'),
]

DRUG_FORM_CHOICES = [
    ('Tablets', 'Tablets'),
    ('Capsules', 'Capsules'),
    ('Gummies', 'Gummies'),
    ('Powdered', 'Powdered'),
    ('Liquid', 'Liquid'),
]

HEALTH_BUDGET_CHOICES = [
    ('NGN1000 - NGN8000', 'NGN1000 - NGN8000'),
    ('NGN8000-NGN15000', 'NGN8000-NGN15000'),
    ('NGN15000 - NGN25000', 'NGN15000 - NGN25000'),
    ('NGN25000 - NGN50000', 'NGN25000 - NGN50000'),
    ('NGN50000 - NGN500000', 'NGN50000 - NGN500000'),
]


# various quiz-classes and definition
class BasicsForm(forms.ModelForm):
    class Meta:
        model = Basic
        fields = ('nickname', 'gender', 'age', 'weight', 'height')
        widgets = {
            'nickname': forms.TextInput(attrs={'placeholder': 'Enter nickname'}),
            'gender': forms.Select(choices=GENDER_CHOICES, attrs={'placeholder': 'Select gender'}),
            'age': forms.Select(choices=AGE_CHOICES, attrs={'placeholder': 'Select age group'}),
            'weight': forms.NumberInput(attrs={'placeholder': 'Enter weight (kg)', 'min': 20, 'max': 200, 'step': 0.1}),
            'height': forms.NumberInput(attrs={'placeholder': 'Enter height (cm)', 'min': 120, 'max': 210, 'step': 0.1}),
        }

class LifestyleForm(forms.ModelForm):
    class Meta:
        model = Lifestyle
        fields = ('habits', 'recreation', 'lifestyle')
        widgets = {
            'habits': forms.SelectMultiple(attrs={'choices': HABIT_CHOICES}),
            'recreation': forms.SelectMultiple(attrs={'choices': RECREATION_CHOICES}),
            'lifestyle': forms.CheckboxSelectMultiple(attrs={'choices': LIFESTYLE_CHOICES}),
        }

class HealthConditionForm(forms.ModelForm):
    class Meta:
        model = HealthCondition
        fields = ('health_complaints', 'current_medications', 'genetic_history', 'allergies', 'health_fears')
        widgets = {
            'health_complaints': forms.CheckboxSelectMultiple(attrs={'choices':HEALTH_COMPLAINT_CHOICES}),
            'current_medications': forms.Textarea,'genetic_history': forms.CheckboxSelectMultiple(attrs={'choices': GENETIC_HISTORY_CHOICES}),
            'allergies': forms.CheckboxSelectMultiple(attrs={'choices': ALLERGY_CHOICES}),
            'health_fears': Textarea(
                attrs={
                    'rows': 5,
                    'cols': 30,
                    'maxlength': 200,
                    'placeholder': 'describe all your health fear as best as you can',
                    'style': 'font-size: 14px;',
                    'class': 'health-fears-textarea'
        }
    ),
}

class PreferenceForm(forms.ModelForm):
    class Meta:
        model = Preference
        fields = ('drug_form', 'health_budget')
        widgets = {
            'drug_form': forms.CheckboxSelectMultiple(attrs={'choices': DRUG_FORM_CHOICES}),
            'health_budget': forms.RadioSelect(attrs={'choices': HEALTH_BUDGET_CHOICES}),
        }

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class meta:
        model = User
        fields =['username','email','password1','password2',]
        
    username= forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email= forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email Address'}))
    password1 = forms.CharField(widget= forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2= forms.CharField(widget= forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )

