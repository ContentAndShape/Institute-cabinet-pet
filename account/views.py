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
            if user_type == 'student':
                user = form.save(commit=False)
                user.is_student = True
                user.save()
            elif user_type == 'teacher':
                user = form.save(commit=False)
                user.is_teacher = True
                user.save()
            else:
                form.save()

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