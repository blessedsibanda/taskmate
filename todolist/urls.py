from django.urls import path
from . import views

urlpatterns = [
     path('', views.todolist, name='todolist'),
     path('delete/<id>', views.delete_task, name='delete_task'),
     path('about/', views.about, name='about'),
     path('contact/', views.contact, name='contact'),
]