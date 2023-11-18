from django.shortcuts import render
from . models import product

def index (request):
    item=product.objects.all()
    return render(request,"index.html",{"item":item})

# Create your views here.
