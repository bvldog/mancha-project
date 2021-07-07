from django.shortcuts import render
from .models import Team


def home(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }

    return render(request, "pages/home.html", data)


def about(request):

    return render(request, 'pages/about.html')


def service(request):
    return render(request, 'pages/service.html')


def contact(request):
    return render(request, 'pages/contact.html')
