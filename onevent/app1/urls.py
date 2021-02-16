from django.urls import path
from app1 import views
from app1.views import EventzDetailView

app_name = 'app1'

urlpatterns = [
    path('', views.acasa, name="home"),
    path('events/', views.HomeIndex.as_view(), name="events"),
    # path('questions/', views.QuestionIndex.as_view(), name="questions"),
    path('adaugare/', views.EventFormAdd.as_view(), name='adaugare'),
    # path('intreaba/', views.question_detail(), name='intreaba'),
    path('<slug:slug>/', views.question_detail, name='askme'),
    path('<pk>/delete/', views.EventsDeleteView.as_view(), name='stergere'),
    path('<pk>/edit_event/', views.UpdateEventsView.as_view(), name="modificare"),
    path('contact/', views.contact1, name='contact'),
    # path('event_live/', views.event_live, name='event_live'),
    path('<int:pk>', EventzDetailView.as_view(), name='event_detail'),
]
