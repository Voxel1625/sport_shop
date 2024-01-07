from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser

from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'photo', 'price']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'content']
    list_editable = ['price']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'photo']
    list_display_links = ['id', 'name']
    search_fields = ['name']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
