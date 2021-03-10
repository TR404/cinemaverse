from django.db import models

# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length = 300)
	description = models.TextField()
	image = models.ImageField(upload_to = 'homeBlog/images', blank = True)
	url = models.URLField(blank = True)
	date = models.DateField()
	
	def __str__(self):
		return self.title
