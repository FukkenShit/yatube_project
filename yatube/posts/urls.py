from django.urls import path, include

from . import views


urlpatterns = [
    path('group/<slug:slug>/', views.group_posts),
    path('', views.index),
]
