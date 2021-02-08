from django.urls import path
from app1 import views

app_name = 'app1'

urlpatterns = [
    path('', views.HomeIndex.as_view(), name="home"),
    path('add_event/', views.CreateIndexView.as_view(), name="Adaugare"),
    path('edit_event/<int:pk>/', views.UpdateLocationView.as_view(), name="Modificare"),
]
