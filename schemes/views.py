

# from django.shortcuts import render
# from .models import Scheme

# def categories_page(request):
#     return render(request, "schemes/schemes_categories.html")

# def scheme_list(request, category):
#     schemes = Scheme.objects.filter(category=category)
#     return render(request, "schemes/schemes_list.html", {"schemes": schemes})

# #for dropdown
# def scheme_by_category(request):
#     category = request.GET.get('category')  # 👈 from dropdown

#     schemes = Scheme.objects.filter(category=category)

#     return render(
#         request,
#         "schemes/schemes_list.html",
#         {
#             "schemes": schemes,
#             "selected_category": category
#         }
#     )

# views.py
from django.shortcuts import render
from .models import Scheme

# View to show all categories
def categories_page(request):
    # Get all distinct categories from Scheme model
    categories = Scheme.objects.values_list('category', flat=True).distinct()

    return render(request, 'schemes/schemes_categories.html', {'categories': categories})

def schemes_list(request, category_name):
    schemes = Scheme.objects.filter(
        category__iexact=category_name,
        status='active'
    )

    return render(request, 'schemes/schemes_list.html', {
        'schemes': schemes,
        'category_name': category_name
    })

     
    
def scheme_by_category(request):
    category = request.GET.get('category')

    schemes = Scheme.objects.filter(category=category)

    print("DEBUG CATEGORY:", category)
    print("DEBUG SCHEMES:", schemes)

    return render(
        request,
        "schemes/schemes_list.html",
        {
            "schemes": schemes,
            "selected_category": category
        }
    )
