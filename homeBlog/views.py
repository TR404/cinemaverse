from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Project
from django.utils import timezone

# Create your views here.

def home(request):
	projects = Project.objects.all()[::-1]
	return render(request, 'homeBlog/home.html', {'projects': projects})
	
	
def detailMovie(request, movieId):
	projects = get_object_or_404(Project, pk = movieId)
	projects.view = projects.view + 1
	projects.save()
	return render(request, 'homeBlog/detailMovie.html', {'projects': projects})
	
def searchbar(request):
	search = request.GET['search']
	projects = Project.objects.filter(title__icontains=search)
	return render(request, 'homeBlog/searchbar.html', {'projects': projects, "search": search})
