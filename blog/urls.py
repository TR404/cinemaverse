from django.urls import path
from .import views

app_name = 'blog'

urlpatterns = [
	path('',views.homeBlog, name = 'homeBlog'),
	path('<int:blogId>/',views.detail, name = 'detail')
]
