from django.shortcuts import render

from simple_page.forms import User_Form

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'simple_page/index.html')

def about_us(request):
    return render(request, 'simple_page/about_us.html')

def register(request):
    
    registered = False

    if request.method == 'POST':
        user_form = User_Form(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True

        else:
            print(user_form.errors)

    else:
        user_form = User_Form()

    return render(request, 'simple_page/registration.html', {
                            'user_form':user_form,
                            'registered':registered
                            })

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
    
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('ACCOUNT IS NOT ACTIVE')

        else:
            print("Some tried tol ogin failed!")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("invalid login details supplied!")

    else:
        return render(request, 'simple_page/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))