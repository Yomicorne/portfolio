from django.shortcuts import render
from .models import Project

def index(request):
    projects = Project.objects.all()
    return render(request, 'main/index.html', {'projects': projects})

def social_media(request):
    return render(request, 'main/social_media.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'main/projects.html', {'projects': projects})

def game(request):
    return render(request, 'main/game.html')
