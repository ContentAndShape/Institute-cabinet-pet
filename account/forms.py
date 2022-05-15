from django import forms
from .models import MyUser, Student, Teacher


class MyRegistrationForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
        ]


class StudentRegistrationForm(forms.ModelForm):   
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
            'institute',
        ]

class TeacherRegistrationForm(forms.ModelForm):
    class Meta(MyRegistrationForm.Meta):
        model = Teacher


class LogInForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=255)
    password = forms.CharField(label='Password', max_length=255)