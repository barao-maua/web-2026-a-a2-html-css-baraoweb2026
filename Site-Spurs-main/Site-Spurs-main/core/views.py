from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def roster(request):
    return render(request, 'core/roster.html')

def history(request):
    return render(request, 'core/history.html')

def arena(request):
    return render(request, 'core/arena.html')
