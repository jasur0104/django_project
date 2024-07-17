from django.urls import path
from .views import login_qismi, register

urlpatterns = [
    path('login/', login_qismi, name='login'),
    path('register/', register, name='register'),
]