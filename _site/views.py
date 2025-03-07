from django.shortcuts import render
from .models import SiteSettings, FirstScreenSettings, AdvantagesScreenSettings


def index(request):
    common = SiteSettings.objects.first()
    first_screen = FirstScreenSettings.objects.first()
    advantages_screen = AdvantagesScreenSettings.objects.first()

    data = {
        'common': common,
        'first_screen': first_screen,
        'advantages_screen': advantages_screen
    }

    return render(request, 'index.html', {'data': data})


def success(request):
    return render(request, 'success.html')


def not_found(request):
    return render(request, '404.html')