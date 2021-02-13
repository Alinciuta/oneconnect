from django.urls import path
from app1 import views

app_name = 'app1'

urlpatterns = [
    path('', views.acasa, name="home"),
    path('evenimente/', views.HomeIndex.as_view(), name="events"),
    path('adaugare/', views.EventFormAdd.as_view(), name='adaugare'),
    path('<pk>/delete/', views.EventsDeleteView.as_view(), name='stergere'),
    path('<pk>/edit_event/', views.UpdateEventsView.as_view(), name="modificare"),
    path('contact/', views.contact1, name='contact'),
    path('preventia_sinuciderii/', views.preventia_sinuciderii, name='preventia_sinuciderii'),
]
