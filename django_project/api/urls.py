from django.urls import path

from .views import EventView, EventListView
from .views import CityListView
from .views import RouteListView, RouteView

urlpatterns = [
    path('api/event', EventListView.as_view(), name='api_event_list'),
    path('api/event/<int:id>',  EventView.as_view(), name='api_event'),

    path('api/city',  CityListView.as_view(), name='api_city_list'),

    path('api/route',  RouteListView.as_view(), name='api_route_list'),
    path('api/route/<int:id>',  RouteView.as_view(), name='api_route'),
]
