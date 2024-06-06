from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
   path('',views.index),
   path('error/',views.error),
   path('contact/',views.contact),
   path('blog/',views.blog),
   path('portfolio/',views.portfolio),
]