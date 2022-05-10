from . import views
from django.urls import path

urlpatterns = [
    path('', views.account, name='account'),
    path('register-<slug:user_type>/', views.registration, name='registration'),
]