from django.urls import path
from . import views

app_name = 'user_registration'

urlpatterns = [
    path('', views.home, name='homepage'),           # ✅ home page
    path('register/', views.register, name='register'),  # registration page
]
