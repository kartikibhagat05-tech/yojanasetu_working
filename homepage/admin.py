

# Register your models here.
from django.contrib import admin
# from .models import Scheme

class SchemeAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')
    search_fields = ('title', 'description')
    list_filter = ('title',)
    ordering = ('title',)

# admin.site.register(Scheme, SchemeAdmin)
