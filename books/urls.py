from django.urls import path
from rest_framework import routers, serializers, viewsets

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('api/books/', views.ListBooks.as_view()),
    path('api/books/<int:pk>/', views.DetailBooks.as_view()),
    path('api/booksdata/', views.booksdata),
]