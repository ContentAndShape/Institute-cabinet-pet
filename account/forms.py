from django.forms import ModelForm
from .models import MyUser, Student, Teacher


class MyRegistrationForm(ModelForm):
    class Meta:
        model = MyUser
        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
        ]


class StudentRegistrationForm(ModelForm):   
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
            'institute',
        ]

class TeacherRegistrationForm(ModelForm):
    class Meta(MyRegistrationForm.Meta):
        model = Teacher
