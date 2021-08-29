from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def index(request):
    return HttpResponse(Article.objects.all())