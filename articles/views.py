from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def index(request):
    context= {
        'person': 'hello world',
        }
    return render(request, 'index.html', context)
    # return HttpResponse(Article.objects.all())