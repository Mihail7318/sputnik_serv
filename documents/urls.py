from django.urls import path
from documents import views


urlpatterns = [
    path('/', views.doc, name='document'),
]
