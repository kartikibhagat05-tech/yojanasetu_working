# homepage/views.py
from django.shortcuts import render
from schemes.models import Scheme


def home(request):
    # Count total schemes
    total_schemes = Scheme.objects.count()

    # Count schemes per category
    category_counts = {}
    for cat_key, cat_name in Scheme.CATEGORY_CHOICES:
        category_counts[cat_key] = Scheme.objects.filter(category=cat_key).count()

    context = {
        'total_schemes': total_schemes,
        'category_counts': category_counts,
    }

    return render(request, 'homepage/home.html', context)


def about(request):
    return render(request, 'homepage/about.html')
