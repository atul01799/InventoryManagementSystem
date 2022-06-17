from django.contrib import admin

# Register your models here.
from .models import *



@admin.register(inventory)
class inventory(admin.ModelAdmin):
    list_display = ['id','name','description','note', 'stock','availability','supplier']
    search_fields = ('id','name','description','note', 'stock','availability','supplier')
 

@admin.register(Supplier)
class Supplier(admin.ModelAdmin):
    list_display = ['id','name']
    search_fields = ('id','name')

