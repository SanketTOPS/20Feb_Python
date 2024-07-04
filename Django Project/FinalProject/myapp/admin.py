from django.contrib import admin
from .models import *

# Register your models here.
class notesData(admin.ModelAdmin):
    list_display=['id','created','title','opt','myfile','desc']

admin.site.register(usersignup)
admin.site.register(notes,notesData)
