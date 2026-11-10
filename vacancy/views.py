from django.shortcuts import render, get_object_or_404
from .models import VacancyCategory, Vacancy


def category_list(request):
    categories = VacancyCategory.objects.all()
    return render(request, 'vacancy/vacancycategories.html', {'categories': categories})


def vacancy_list(request, slug):
    category = get_object_or_404(VacancyCategory, slug=slug)
    vacancies = category.vacancies.filter(is_active=True)
    return render(request, 'vacancy/vacancylist.html', {'category': category, 'vacancies': vacancies})
