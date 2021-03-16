from django.urls import path
from .import views

app_name = 'homeBlog'

urlpatterns = [
	path('<int:movieId>/',views.detailMovie, name = 'detailMovie'),
	path('search/', views.searchbar, name = 'searchbar'),
]
