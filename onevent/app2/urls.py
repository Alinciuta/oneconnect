from django.urls import path

from app2 import views

app_name = 'app2'

urlpatterns = [
    path('<slug:slug>/', views.post_detail, name='post_detail')
]
