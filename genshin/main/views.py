from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')


def news(request):
    return render(request, 'news/news_home.html')


def pers(request):
    return render(request, 'gallery/pers.html')
