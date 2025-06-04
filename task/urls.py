from django.urls import path
from . import views

urlpatterns = [
    path('', views.ipexam_list, name='ipexam-list'),
]