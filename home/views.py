from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session
from user.forms import BasicsForm, LifestyleForm, HealthConditionForm, PreferenceForm
# from user.models import Notification
def homepage(request):
    # Check if the user is not logged in
    if not request.user.is_authenticated:
   
        return render(request, 'home/home.html', )

    # If the user is logged in, proceed with the notifications logic
    # notifications = request.user.notifications.order_by('-created_at')
    # x  = Notification.objects.get(user=request.user)
    # Reset the new notifications count
    user_profile = request.user.profile
    

    user_profile.new_notifications_count = 0
    user_profile.save()

    # Mark notifications as read
    # notifications.update(is_read=True)

    return render(request, 'home/home.html', )


    # return render(request, 'home/home.html', {'notifications': notifications})
def handle_continue_quiz(request):
    form_type = request.POST.get('form_type')
    print(form_type)
    
    if form_type == 'basics':
        request.session['basics'] = request.POST
    if form_type == 'lifestyle':
        request.session['lifestyle'] = request.POST
    if form_type == 'health_condition':
        request.session['health_condition'] = request.POST
    if form_type == 'preference':
        request.session['preference'] = request.POST
    
    return redirect ('/quiz/')

def handle_request_dashboard(request):
    form_type = request.POST.get('form_type')
    
    # Retrieve saved session data
    basics = request.session.get('basics', {})
    lifestyle = request.session.get('lifestyle', {})
    health_condition = request.session.get('health_condition', {})
    preference = request.session.get('preference', {})
    
    # Update current form data
    if form_type == 'basics':
        request.session['basics'] = request.POST
    if form_type == 'lifestyle':
        request.session['lifestyle'] = request.POST
    if form_type == 'health_condition':
        request.session['health_condition'] = request.POST
    if form_type == 'preference':
        request.session['preference'] = request.POST
    
    return redirect('user:register')

def quiz_page(request):
    if request.method == 'POST':
        if 'continue_quiz' in request.POST:
            return handle_continue_quiz(request)
        elif 'request_dashboard' in request.POST or 'quiz_submit' in request.POST:
            return handle_request_dashboard(request)
    
    # Handle GET requests or render the quiz page
    return render(request, 'quiz/quiz.html', {
        'basics_form': BasicsForm(),
        'lifestyle_form': LifestyleForm(),
        'health_condition_form': HealthConditionForm(),
        'preference_form': PreferenceForm() 
    })
