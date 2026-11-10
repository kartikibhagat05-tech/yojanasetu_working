from django.db import models
from django.utils.text import slugify


class VacancyCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Vacancy Categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    title = models.CharField(max_length=300)
    category = models.ForeignKey(
        VacancyCategory,
        on_delete=models.CASCADE,
        related_name='vacancies'
    )
    department = models.CharField(max_length=200)
    source = models.CharField(max_length=100)
    job_location = models.CharField(max_length=100, default='All India')
    total_posts = models.IntegerField(null=True, blank=True)
    salary = models.CharField(max_length=100, null=True, blank=True)
    last_date = models.DateField(null=True, blank=True)
    apply_link = models.URLField()
    notification_pdf = models.URLField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Vacancies'

    def __str__(self):
        return self.title
