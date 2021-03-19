from django.db import models

# Create your models here.

class Project(models.Model):
	title = models.CharField(max_length = 100)
	description = models.TextField()
	image = models.ImageField(upload_to = 'homeBlog/images')
	sst1 = models.ImageField(upload_to = 'homeBlog/images', blank = True)
	sst2 = models.ImageField(upload_to = 'homeBlog/images', blank = True)
	sst3 = models.ImageField(upload_to = 'homeBlog/images', blank = True)
	sst4 = models.ImageField(upload_to = 'homeBlog/images', blank = True)
	sst5 = models.ImageField(upload_to = 'homeBlog/images', blank = True)
	url = models.URLField(blank = True)
	url42 = models.URLField(blank = True)
	url72 = models.URLField(blank = True)
	url10 = models.URLField(blank = True)
	view = models.IntegerField(default = 0)
	
	def __str__(self):
		return self.title

