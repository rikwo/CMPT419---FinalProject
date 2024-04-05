from django.urls import path
from .views import main 

urlpatterns = [
    path('login/', views.spotify_login, name='spotify_login'),
    path('quiz/', views.quiz, name='quiz'),
]