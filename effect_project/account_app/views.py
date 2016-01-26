from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.contrib.auth import login as django_login, authenticate, logout as django_logout


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
            user = authenticate(email=request.POST['email'],
                                password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    return redirect('/')
    else:
        form = AuthenticationForm()
    return render_to_response('account_app/login.html',{
        'form': form,
    }, context_instance=RequestContext(request))

def register(request):
    """
    Registration view
    """
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/')
    else:
        form = RegistrationForm()
    return render_to_response('account_app/register.html',{
        'form': form,
    }, context_instance=RequestContext(request))

def logout(request):
    """
    Logout view
    """
    django_logout(request)
    return redirect('/')