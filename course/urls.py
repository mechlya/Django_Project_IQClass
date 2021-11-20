from django.urls import path, include
from . import views

app_name = 'course'
urlpatterns = [
    
    path('', views.course_list, name = 'course_list'),
    path('<str:slug>', views.course_detail, name= 'course_detail' ),

       
    
]