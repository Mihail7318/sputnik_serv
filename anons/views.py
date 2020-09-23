from django.shortcuts import render


def anons(request):
    return render(request, 'anons.html')

def video(request):
    return render(request, 'base.html')
# Create your views here.
