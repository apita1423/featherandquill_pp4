from django.urls import path
from . import views


# Code Credit: Dennis Ivy (Link in README)
urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('add/', views.addPhoto, name='add'),
]