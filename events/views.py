from django.shortcuts import render
from .models import event, PostsImages
from news.models import article
from django.db.models import F


# Create your views here.
def events(request):
    events = event.objects.order_by('-date')
    # images = PostsImages.objects.filter(event__id=F('event__id'))
    # images = event.images.all()
    return render(request, "events.html", {'events': events})


def events_prev(request, pk):
    event_detail = event.objects.filter(id=pk)
    read = event.objects.all()[:5]
    return render(request, "detail.html",{"data":event_detail, 'read':read})

