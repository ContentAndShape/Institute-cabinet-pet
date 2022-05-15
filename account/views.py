from django.contrib import messages
from django.contrib.auth import hashers, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import (
    MyRegistrationForm,
    StudentRegistrationForm,
    TeacherRegistrationForm,
    LogInForm,
)


def registration(request, user_type):
    if request.method == 'POST':

        if user_type == 'student':
            form = StudentRegistrationForm(request.POST)
        elif user_type == 'teacher':
            form = TeacherRegistrationForm(request.POST)
        elif user_type == 'user':
            form = MyRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.password = hashers.make_password(request.POST['password'])

            if user_type == 'student':
                user.is_student = True
            elif user_type == 'teacher':
                user.is_teacher = True

            user.save()
            user_email = form.cleaned_data.get('email')
            messages.success(request, f'Registered user {user_email}')
            return redirect('account')

    else:
        if user_type == 'student':
            form = StudentRegistrationForm()
        elif user_type == 'teacher':
            form = TeacherRegistrationForm()
        elif user_type == 'user':
            form = MyRegistrationForm()

        context = {
            'form': form,
        }
    
    return render(request, 'account/registration.html', context)


def authentication(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)

        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'Successfull login {user.first_name, user.last_name}')
                return redirect('account')
            else:
                messages.error(request, 'Incorrect username or password')
                return redirect('login')
    else:
        form = LogInForm()
        user = request.user
        context = {
            'form': form,
            'user': user,
        }
        return render(request, 'account/login.html', context)


def account(request):
    context = {
        'user': request.user,
    }
    return render(request, 'account/base.html', context)