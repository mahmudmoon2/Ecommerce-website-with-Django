from django.shortcuts import render
from . models import Category
# Create your views here.
def home(request):
    categories = Category.objects.all()
    return render(request, 'products/home.html' , {'categories': categories})

