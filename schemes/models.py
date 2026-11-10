from django.db import models

class Scheme(models.Model):
    CATEGORY_CHOICES = [
        ('education', 'Education'),
        ('women', 'Women Welfare'),
        ('farmer', 'Farmer'),
        ('health', 'Health'),
        ('housing', 'Housing'),
        ('loan', 'Loan'),
        ('scholarship', 'Scholarship'),
        ('employment', 'Employment'),
        ('disability', 'Disability'),
        ('senior', 'Senior Citizen'),
        ('business', 'Business'),
        ('general', 'General Schemes'),
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('expired', 'Expired'),
    ]

    name = models.CharField(max_length=255, default="Not specified")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="general")
    type = models.CharField(max_length=20, default="central")  # central / state
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")
    duration = models.CharField(max_length=200, default="Not specified")
    eligibility = models.TextField(default="Not specified")
    age_requirement = models.IntegerField(default=18)
    documents_required = models.TextField(default="Not specified")
    official_link = models.URLField(default="https://www.example.com")

    def __str__(self):
        return self.name
