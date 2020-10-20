from django.urls import path

from . import views

app_name = 'MMblog'
urlpatterns = [
    path('', views.home, name='home'),
    path('o-mnie/', views.about_me, name='about_me'),
    path('projekty/', views.projects, name='projects'),
    path('kontakt/', views.contact, name='contact'),
    path('<str:slug>/', views.viewing_post, name='viewing_post'),
]