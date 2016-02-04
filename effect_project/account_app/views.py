from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import login as django_login, authenticate, logout as django_logout
from account_app.forms import UserCreationForm, AuthenticationForm


def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'account_app/index.html', context_dict)

def login(request):
    """
    Login view
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(email=email, password=password)

            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    return HttpResponseRedirect('/account/')
                else:
                    return HttpResponse("Your account is disabled.")
            else:
                return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'account_app/login.html', {})

def register(request):
    """
    Registration view
    """
    registered = False
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
    else:
        form = UserCreationForm()
    return render(request,
                  'account_app/register.html',
                  {'form': form, 'registered': registered})

def logout(request):
    """
    Logout view
    """
    django_logout(request)
    return redirect('/')