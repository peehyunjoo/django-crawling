from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # views.index => views.py의 index함수
    path('signup/', views.signup),
    path('main/', views.main, name='main'),
]