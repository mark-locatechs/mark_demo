from django.urls import path, include

from .views import DashboardView, LoremView

urlpatterns = [
    path('', DashboardView.as_view(), name='index'),
    path('lorem', LoremView.as_view(), name='lorem'),
    path('accounts/', include('django.contrib.auth.urls')),
]
