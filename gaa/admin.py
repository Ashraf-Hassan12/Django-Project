from django.contrib import admin
from .models import product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock','image_url')

admin.site.register(product,ProductAdmin)