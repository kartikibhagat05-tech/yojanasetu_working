# user_registration/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages

from .models import CustomUser, CATEGORY_CHOICES


def register(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name', '')
        age = request.POST.get('age', None)
        gender = request.POST.get('gender', '')
        photo = request.FILES.get('photo')
        primary_category = request.POST.get('primary_category', 'general')
        occupation = request.POST.get('occupation', '')
        phone = request.POST.get('phone', '')
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')
        notify = 'notify' in request.POST
        eligible_categories = request.POST.getlist('eligible_categories')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('user_registration:register')

        if CustomUser.objects.filter(phone=phone).exists():
            messages.error(request, "A user with this phone number already exists.")
            return redirect('user_registration:register')

        # Convert eligible categories list to comma-separated string
        eligible_str = ",".join(eligible_categories)

        user = CustomUser.objects.create_user(
            username=phone,
            full_name=full_name,
            age=age if age else None,
            gender=gender,
            photo=photo,
            primary_category=primary_category,
            eligible_categories=eligible_str,
            occupation=occupation,
            phone=phone,
            notify=notify,
            password=password
        )

        login(request, user)
        messages.success(request, "Registration successful! Welcome to Yojana Setu.")
        return redirect('homepage:home')

    return render(request, 'user_registration/registration_form.html', {
        'categories_choices': CATEGORY_CHOICES
    })


def home(request):
    return render(request, 'homepage/home.html')
