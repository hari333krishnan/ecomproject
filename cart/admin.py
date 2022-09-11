from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(CartList)
admin.site.register(CartItems)


