from django.contrib import admin

from .models import Student, Teacher, Institute, Course

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Institute)
admin.site.register(Course)