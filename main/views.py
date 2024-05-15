from django.shortcuts import render
from . import models


def home(request):
    zaprafka = models.Zaprafka.objects.all()
    context = {
        'zaprafka_list': zaprafka,
    }
    return render(request, 'home.html', context)


def detail(request, id):
    zaprafka = models.Zaprafka.objects.get(id=id)
    context = {
        'zaprafka': zaprafka,
    }
    return render(request, 'detail.html', context)
