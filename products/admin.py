from django.contrib import admin
from .models import Products
 
# Register your models here.
@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display =['id','name','weight','price','created_at','updated_at']
