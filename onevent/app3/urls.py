from django.urls import path

from app3 import views

app_name = 'app3'

urlpatterns = [
    path('questionaire/', views.FeedbackFormAdd.as_view(), name='questionaire'),
    path('feedback_complete/', views.completed, name='feedback_complete'),
]
