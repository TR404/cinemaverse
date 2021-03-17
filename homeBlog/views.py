from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Project, User
from django.utils import timezone
from django.db.models import Q

# Create your views here.

def home(request):
	projects = Project.objects.all()[::-1]
	return render(request, 'homeBlog/home.html', {'projects': projects})
	
	
def detailMovie(request, movieId):
	projects = get_object_or_404(Project, pk = movieId)
	def get_ip(request):
		address = request.META.get('HTTP_X_FORWARDED_FOR')
		if address:
			ip = address.split(',')[-1].strip()
		else:
			ip = request.META.get('REMOTE_ADDR')
		return ip
	ip = get_ip(request)
	u = User(user = ip)
	result = User.objects.filter(Q(user__icontains= ip))
	if len(result)==1:
		pass
	elif len(result)>1:
		pass
	else:
		u.save()
	count = User.objects.all().count()
	return render(request, 'homeBlog/detailMovie.html', {'projects': projects, 'count': count})
	
def searchbar(request):
	search = request.GET['search']
	projects = Project.objects.filter(title__icontains=search)
	return render(request, 'homeBlog/searchbar.html', {'projects': projects, "search": search})
