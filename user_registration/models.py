# from django.contrib.auth.models import AbstractUser
# from django.db import models


# CATEGORY_CHOICES = [
#     ('education', 'Education'),
#     ('women', 'Women'),
#     ('farmer', 'Farmer'),
#     ('health', 'Health'),
#     ('housing', 'Housing'),
#     ('loan', 'Loan'),
#     ('scholarship', 'Scholarship'),
#     ('employment', 'Employment'),
#     ('disability', 'Disability'),
#     ('senior', 'Senior Citizen'),
#     ('business', 'Business'),
#     ('general', 'General'),
# ]

# class CustomUser(AbstractUser):
#     full_name = models.CharField(max_length=150)
#     age = models.PositiveIntegerField()
#     gender = models.CharField(max_length=20)
#     photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
#     primary_category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
#     # Store multiple categories as comma-separated string
#     eligible_categories = models.TextField(blank=True, help_text="Comma separated categories (education, health, etc.)")
#     occupation = models.CharField(max_length=100)
#     phone = models.CharField(max_length=10, unique=True)
#     notify = models.BooleanField(default=True)

#     USERNAME_FIELD = 'username'  # default
#     REQUIRED_FIELDS = ['full_name', 'phone']

#     def __str__(self):
#         return self.username

from django.contrib.auth.models import AbstractUser
from django.db import models

CATEGORY_CHOICES = [
    ('education', 'Education'),
    ('women', 'Women'),
    ('farmer', 'Farmer'),
    ('health', 'Health'),
    ('housing', 'Housing'),
    ('loan', 'Loan'),
    ('scholarship', 'Scholarship'),
    ('employment', 'Employment'),
    ('disability', 'Disability'),
    ('senior', 'Senior Citizen'),
    ('business', 'Business'),
    ('general', 'General'),
]

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=150, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=20, blank=True)

    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    primary_category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='general'
    )

    eligible_categories = models.TextField(
        blank=True,
        help_text="Comma separated categories (education, health, etc.)"
    )

    occupation = models.CharField(max_length=100, blank=True)

    phone = models.CharField(max_length=10, unique=True, null=True, blank=True)

    notify = models.BooleanField(default=True)

    def __str__(self):
        return self.username
