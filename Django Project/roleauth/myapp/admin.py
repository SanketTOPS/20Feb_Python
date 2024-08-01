from django.contrib import admin
from .models import *

# Register your models here.

class userData(admin.ModelAdmin):
    list_display=['id','role','firstname','lastname','username','password']

admin.site.register(users,userData)