from django.shortcuts import render
from django.shortcuts import render
from .models import Beach

def home(request):
    beaches = Beach.objects.all()
    return render(request, 'home.html', {'beaches': beaches})
# Create your views here.
