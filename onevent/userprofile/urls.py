from django.urls import path
from userprofile import views

app_name = 'userprofile'

urlpatterns = [
    path('new_account/', views.CreateUser.as_view(), name="new_account"),
]