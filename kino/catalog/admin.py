from django.contrib import admin

# Register your models here.

from .models import Film, Type

admin.site.register(Film)
admin.site.register(Type)

# python manage.py createsuperuser

