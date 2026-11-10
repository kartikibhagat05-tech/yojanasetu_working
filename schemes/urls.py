from django.urls import path
from . import views

urlpatterns = [
    path('', views.categories_page, name='scheme_categories'),  # URL name fixed
    # path('<str:category>/', views.scheme_list, name='scheme_list'),
    # path('list/', views.scheme_by_category, name='scheme_by_category'),
    path("by-category/", views.scheme_by_category, name="scheme_by_category"),
    # path('category/<int:category_id>/', views.schemes_list, name='schemes_list'),
     path('<str:category_name>/', views.schemes_list, name='schemes_list'),
]
