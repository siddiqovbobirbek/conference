from django.shortcuts import render

def home(request):
    context = {}
    return render(request, "home.html", context)

def uz(request):
    context = {}
    return render(request, "uz.html", context)

def ru(request):
    context = {}
    return render(request, "ru.html", context)

def en(request):
    context = {}
    return render(request, "eng.html", context)

    
