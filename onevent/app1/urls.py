from django.urls import path
from app1 import views

app_name = 'app1'

urlpatterns = [
    path('', views.HomeIndex.as_view(), name="home"),
    path('adaugare/', views.EventFormAdd.as_view(), name='adaugare'),
]
