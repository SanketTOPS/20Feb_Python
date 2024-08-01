from django.contrib import admin
from .models import *

# Register your models here.

class productDetails(admin.ModelAdmin):
    list_display=['pname','price','ram','pmodel','img']


admin.site.register(product_master)
admin.site.register(sub_category,productDetails)