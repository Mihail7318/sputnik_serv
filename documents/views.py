from django.shortcuts import render
from .models import Document
# Create your views here.
def doc(request):
    document = Document.objects.all()
    return render(request, 'document.html', {'doc':document})