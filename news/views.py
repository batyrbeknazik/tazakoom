from django.shortcuts import render
from django.views import generic
from . import models

# Create your views here.
class MainPage(generic.ListView):
    model = models.News
    template_name = 'headers/main.html'