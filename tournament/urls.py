from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.login_view, name='login'),   # login first
    path('dashboard/', views.dashboard, name='dashboard'),
    path('members/', views.members, name='members'),
    path('tournaments/', views.tournament_list, name='tournament_list'),
    path('tournaments/<int:pk>/', views.tournament_detail, name='tournament_detail'),
    path('news/', views.news_room, name='news_room'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('profile/', views.profile_view, name='profile'),
]