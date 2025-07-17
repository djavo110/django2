from django.shortcuts import render
from django.http import HttpResponse
from .models import * 

def index(request):
    reg = Region.objects.all()
    tum = Tuman.objects.all()
    mah = mahalla.objects.all()

    context = {
        "title": "REG TITLE",
        "reg": reg,
        "tum": tum,
        "mah": mah

    }

    return render(request, 'index.html', context=context)

