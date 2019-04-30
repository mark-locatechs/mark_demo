from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie


class DashboardView(TemplateView):
    template_name = 'index.html'

    @method_decorator(ensure_csrf_cookie)
    def get(self, request):
        return render(request, self.template_name)


@method_decorator(login_required, name='dispatch')
class LoremView(TemplateView):
    template_name = 'lorem.html'

    def get(self, request):
        return render(request, self.template_name)

