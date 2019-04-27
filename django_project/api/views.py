from django.http import JsonResponse
from django.views.generic import TemplateView
import requests, json

from django.conf import settings



class CityListView(TemplateView):
    def get(self, request):

        resp = requests.get(settings.API_BASE_URL + 'city')

        data = json.loads(resp.text)
        return JsonResponse(data, status=resp.status_code)


class RouteListView(TemplateView):

    def get(self, request):
        resp = requests.get(settings.API_BASE_URL + 'route')
        data = json.loads(resp.text)
        return JsonResponse(data, status=resp.status_code)

    def post(self, request):
        resp = requests.post(settings.API_BASE_URL + 'route')
        data = json.loads(resp.text)
        return JsonResponse(data, status=resp.status_code)

class RouteView(TemplateView):
    def get(self, request, id):
        resp = requests.get(settings.API_BASE_URL + 'route/%s' % id)
        data = json.loads(resp.text)
        return JsonResponse(data, status=resp.status_code)

    def delete(self, request, id):
        resp = requests.delete(settings.API_BASE_URL + 'route/%s' % id)
        data = json.loads(resp.text)
        return JsonResponse(data, status=resp.status_code)


class EventListView(TemplateView):

    def get(self, request):
        resp = requests.get(settings.API_BASE_URL + 'event')
        data = json.loads(resp.text)
        return JsonResponse(data, status=resp.status_code)

    def post(self, request):

        request_data = json.loads(request.body)

        resp = requests.post(settings.API_BASE_URL + 'event', json=request_data)

        data = json.loads(resp.text)
        return JsonResponse(data, status=resp.status_code)


class EventView(TemplateView):

    def get(self, request, id):
        resp = requests.get(settings.API_BASE_URL + 'event/%s' % id)
        data = json.loads(resp.text)
        return JsonResponse(data, status=resp.status_code)


    def delete(self, request, id):
        resp = requests.delete(settings.API_BASE_URL + 'event/%s' % id)
        data = json.loads(resp.text)
        return JsonResponse(data, status=resp.status_code)

    def put(self, request, id):

        request_data = json.loads(request.body)
        resp = requests.put(settings.API_BASE_URL + 'event/%s' % id, json=request_data)

        data = json.loads(resp.text)
        return JsonResponse(data, status=resp.status_code)


