from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import UserLoginForm, SignupForm
from .models import Users


# user signup and save user to database
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            user = Users.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email,
                                             password1=password1, password2=password2)

            user.set_password(password1)
            user.save()

            if user is not None:
                print('user created successfully')
            else:
                print('user not created')

            return redirect('login')
    else:
        form = SignupForm()
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            print(username, password)
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                print('user not found')
                return redirect('login')
    else:
        form = UserLoginForm()
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('login')


def profile_page(request):
    return render(request, 'users/profile.html', context={'user_profile': request.user})
