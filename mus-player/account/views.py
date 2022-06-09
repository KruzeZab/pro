from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages, auth
from django.contrib.auth import logout
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('song:index', pk=1)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return HttpResponseRedirect('/1/')
        else:
            messages.error(request, 'Invalid credentials')
            return HttpResponseRedirect('/account/login')
    else:
        return render(request, 'account/login.html')

def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/1/')
    if request.method == 'POST':
        # Get form values
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
        # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return HttpResponseRedirect('/account/register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return HttpResponseRedirect('/account/register')
                else:
                    # Looks good
                    user = User.objects.create_user(username=username, password=password,email=email)
                    # Login after register
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in')
                    return HttpResponseRedirect('/1/')
                    
        else:
            messages.error(request, 'Passwords do not match')
            return HttpResponseRedirect('/account/register')
    else:
        return render(request, 'account/register.html')


def logoutView(request):
    messages.success(request, 'You are now logged out!')
    logout(request)
    return HttpResponseRedirect('/account/login')