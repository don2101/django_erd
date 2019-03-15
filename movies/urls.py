from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('<int:movie_number>/', views.movie_detail, name='movie_detail'),
    path('<int:movie_number>/update/', views.movie_update, name='movie_update'),
    path('<int:movie_number>/delete/', views.movie_delete, name='movie_delete'),
    path('<int:movie_number>/scores/new/', views.score_create, name='score_create'),
    path('<int:movie_number>/scores/<int:score_number>/delete/', views.score_delete, name='score_delete'),
]