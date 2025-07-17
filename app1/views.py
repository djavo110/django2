from django.shortcuts import render
from django.http import HttpResponse
from .models import * 

def index(request):
    reg = Region.objects.all()
    context = {
        "title": "REG TITLE",
        "context": reg
    }

    return render(request, 'index.html', context=context)