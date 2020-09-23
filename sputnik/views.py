from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from news.models import article, covid
from events.models import event
from afisha.models import afisha, holiday
from documents.models import Uslugi
from video.models import Video
from django.db.models import Q



def index(request):

    date_n = datetime.now().date()
    merop = event.objects.order_by('-date')[0:3]
    merop2 = event.objects.order_by('-date')[3:6]
    merop3 = event.objects.order_by('-date')[6:9]
    info = covid.objects.all
    articles = article.objects.order_by('-date_a')[:10]
    afisha_list = afisha.objects.filter(Q(date_out__gte = date_n) & Q(date_in__lte = date_n))
    holiday_list = holiday.objects.filter(date_h__gte=date_n)
    video = Video.objects.order_by('-date')
    return render(request, "index.html",
                  {'merop': merop, 'merop2': merop2, 'merop3': merop3, 'info': info, 'articels': articles, 'afisha': afisha_list, 'holiday':holiday_list, 'vid': video})

def info(request):
    return render(request, "information.html")


def usl(request):
    uslugi = Uslugi.objects.order_by("-date")
    return render(request, "uslugi_two.html", {'usl': uslugi})

def usl_p(request, pk):
    usl = Uslugi.objects.filter(id = pk)
    return render(request, "uslugi.html", {'usl':usl})

