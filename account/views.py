from django.contrib.auth import hashers
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import (
    MyRegistrationForm,
    StudentRegistrationForm,
    TeacherRegistrationForm,
)


def registration(request, user_type):
    if request.method == 'POST':

        if user_type == 'student':
            form = StudentRegistrationForm(request.POST)
        elif user_type == 'teacher':
            form = TeacherRegistrationForm(request.POST)
        else:
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

    elif user_type == 'student':
        form = StudentRegistrationForm()
    elif user_type == 'teacher':
        form = TeacherRegistrationForm()
    else:
        form = MyRegistrationForm()
    
    return render(request, 'account/registration.html', {'form': form})


def account(request):
    return render(request, 'account/base.html')