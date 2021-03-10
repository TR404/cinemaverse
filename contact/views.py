from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
# Create your views here.

def index(request):
	preComment = Contact.objects.all()
	if request.method =="POST":

		contact = Contact()
		email = request.POST.get('email')
		detail = request.POST.get('detail')
		name = request.POST.get('name')
		contact.email=email
		contact.detail=detail
		contact.name=name
		contact.save()
		preComment = Contact.objects.all()[::-1]
		return render(request,'index.html',{'preComment':preComment})
		
	return render(request,'index.html',{'preComment':preComment})
