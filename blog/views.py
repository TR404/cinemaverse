from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def homeBlog(request):
	blogs = Blog.objects.order_by('-date')
	return render(request, 'blog/blogHome.html', {'blogs': blogs})
	
def detail(request, blogId):
	blog = get_object_or_404(Blog, pk = blogId)
	return render(request, 'blog/detail.html', {'blog': blog})
