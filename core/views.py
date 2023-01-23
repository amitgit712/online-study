from django.shortcuts import render
from notes.models import Category

def home(request):
    context = {
        "category": Category.objects.all()
    }
    return render(request, 'core/index.html', context)