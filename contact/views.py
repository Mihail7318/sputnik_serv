from django.shortcuts import render,redirect
from .forms import AboutForm


def index(request):
    about = AboutForm()
    if request.method == "POST":
        aboutform = AboutForm(request.POST)
        if aboutform.is_valid():
            name = aboutform.cleaned_data["name"]
            print(name)
            return render(request, 'about.html', {'name':name, 'form':about})
    return render(request, "about.html", {"form": about})


# Create your views here.
