from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # views.index => views.py의 index함수
    path('signup/', views.signup),
    path('main/', views.main, name='main'),
    path('login/', views.login, name='login'),
    path('login_success/', views.login_success),
    path('logout/', views.logout),
    path('crawling/', views.crawling),
]