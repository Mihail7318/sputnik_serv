from django.shortcuts import render
from .models import article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def news(request):
    object_list = article.objects.all().order_by('-date_a')
    #articles = article.objects.all().order_by('-date_a')
    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, поставим первую страницу
        posts = paginator.page(1)
    except EmptyPage:
        # Если страница больше максимальной, доставить последнюю страницу результатов
        posts = paginator.page(paginator.num_pages)
    return render(request, "news.html", {'page':page, 'articels':posts})


# Create your views here.
def news_prev(request, pk):
    news = article.objects.filter(id=pk).get()
    read = article.objects.exclude(id=pk)[:5]
    return render(request, "detail_news.html", {'data': news, 'read':read})
