from django.http import JsonResponse
from django.views.generic import TemplateView


class EventView(TemplateView):
    def get(self, request):
        return JsonResponse({'a':'b'})

class EventListView(TemplateView):
    def get(self, request):
        return JsonResponse({'a':'b'})
