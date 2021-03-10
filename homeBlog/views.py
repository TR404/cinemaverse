from django.shortcuts import render, get_object_or_404
from .models import Project
from django.utils import timezone

# Create your views here.

def home(request):
	projects = Project.objects.all()[::-1]
	return render(request, 'homeBlog/home.html', {'projects': projects})
	
	
def detailMovie(request, movieId):
	projects = get_object_or_404(Project, pk = movieId)
	return render(request, 'homeBlog/detailMovie.html', {'projects': projects})
