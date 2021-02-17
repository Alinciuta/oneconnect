from django.urls import path
from app1 import views
from app1.views import EventzDetailView

app_name = 'app1'

urlpatterns = [
    path('acasa/', views.acasa, name="home"),
    path('events/', views.HomeIndex.as_view(), name="events"),
    path('adaugare/', views.EventFormAdd.as_view(), name='adaugare'),
    path('<pk>/delete/', views.EventsDeleteView.as_view(), name='stergere'),
    path('<pk>/edit_event/', views.UpdateEventsView.as_view(), name="modificare"),
    path('contact/', views.contact1, name='contact'),
    path('', EventzDetailView.as_view(), name='event_detail'),
]
