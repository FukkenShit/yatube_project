from django.urls import path, include

from . import views

app_name = 'posts'

urlpatterns = [
    path('group/<slug:slug>/', views.group_posts, name='group'),
    path('', views.index, name='index'),
]
