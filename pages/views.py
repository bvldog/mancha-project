from django.shortcuts import render


def pages(request):
    return render(request, "pages/home.html")
