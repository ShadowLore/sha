from django.shortcuts import render


def pers(request):
    return render(request, 'gallery/pers.html')
