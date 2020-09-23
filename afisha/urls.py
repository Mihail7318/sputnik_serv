
from django.contrib import admin
from django.urls import path
from afisha import views


urlpatterns = [
    path('/', views.afisha_detail, name='afisha'),
    path('/<int:pk>', views.holiday_detail, name='holiday')
]
