from django.urls import path

from app2 import views

app_name = 'app2'

urlpatterns = [
    path('questions/', views.Questions.as_view(), name='intrebarile'),
]
