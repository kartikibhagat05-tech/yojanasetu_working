from django.db import models


# CATEGORY_CHOICES used by homepage models only (Scheme model is in schemes app)
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
