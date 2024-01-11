from django.shortcuts import render
import datetime

def current_time(request):
    now = datetime.datetime.now()
    return render(request, 'current_time.html', {'current_time': now})

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
