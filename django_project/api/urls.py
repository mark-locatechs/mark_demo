from django.urls import path

from .views import EventView, EventListView

urlpatterns = [
    path('api/event', EventListView.as_view(), name='api_event_list')
]
