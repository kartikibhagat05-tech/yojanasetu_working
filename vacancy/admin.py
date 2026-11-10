from django.contrib import admin
from .models import VacancyCategory, Vacancy

@admin.register(VacancyCategory)
class VacancyCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('name',)

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'department', 'job_location', 'last_date', 'is_active')
    list_filter = ('category', 'is_active', 'job_location')
    search_fields = ('title', 'department', 'source')
    date_hierarchy = 'last_date'
