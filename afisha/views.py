from django.shortcuts import render
from .models import afisha, holiday
from datetime import datetime
from django.db.models import Q
# Create your views here.

def afisha_detail(request):
    date_n = datetime.now().date()
    films = afisha.objects.filter(Q(date_out__gte = date_n) & Q(date_in__lte = date_n))
    ship = films.first()
    return render(request, "afisha-s.html", {'films': films, 'ship':ship})

def holiday_detail(request, pk):
    hol = holiday.objects.filter(id = pk)
    return render(request, "holiday.html", {'hol': hol})

