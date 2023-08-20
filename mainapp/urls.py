from django.urls import path
from . import views

urlpatterns = [
    path('', views.layout, name='home'),
    path('index/', views.index, name='file'),
    path('about/', views.about, name='about'),
]
