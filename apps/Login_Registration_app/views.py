from django.shortcuts import render, redirect

from __future__ import unicode_literals

from .models import User
# Create your views here.

def index(request):
    context = {
    "user" : User.objects.all()
    }
    return render(request, 'Login_Registration_app/index.html', context)

def register(request):

    if password != request.POST['conf_pwd']:
        messages.errors(request, "Passwords do not match.")

    else:
        postData = {
            "first_name" : request.POST['first_name'],
            "last_name" : request.POST['last_name'],
            "email" : request.POST['email'],
            "password" : request.POST['password'],
        }

    user_array = User.objects.register(postData)

# user_array = [False, [first_name is too short, 'password is too short']]
    if user_array[0] == False:
        for error_message in user_array[1]:
            messages.error(request, error_message)
        return redirect('/')
# redirect to back to registration page.

    print user
# redirect back to success page.
    else:
        return redirect('/')

def login(request):
    
