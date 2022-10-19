from django.contrib import admin

from items.models import Category, Item, Comment

# Register your models here.
admin.site.register([Item, Category, Comment])