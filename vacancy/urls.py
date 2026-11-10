from django.urls import path
from . import views

app_name = 'vacancy'

urlpatterns = [
    path('categories/', views.category_list, name='category_list'),
    path('category/<slug:slug>/', views.vacancy_list, name='vacancy_list'),
]
