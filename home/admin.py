from django.contrib import admin

# Register your models here.
from home.models import *


class CatAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Categ, CatAdmin)


class ProdAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','category','img',]
    list_editable = ['price','stock','available','category','img',]
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Products, ProdAdmin)
