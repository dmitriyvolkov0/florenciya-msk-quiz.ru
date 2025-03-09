from django.shortcuts import render
from .models import SiteSettings, FirstScreenSettings, AdvantagesScreenSettings, FooterScreenSettings


def index(request):
    common = SiteSettings.objects.first()
    first_screen = FirstScreenSettings.objects.first()
    advantages_screen = AdvantagesScreenSettings.objects.first()
    footer_screen = FooterScreenSettings.objects.first()

    data = {
        'common': common,
        'first_screen': first_screen,
        'advantages_screen': advantages_screen,
        'footer_screen': footer_screen
    }

    return render(request, 'index.html', {'data': data})


def success(request):
    return render(request, 'success.html')


def not_found(request):
    return render(request, '404.html')