from django.urls import path
from . import views

app_name = 'simple_page'

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us/', views.about_us, name='about_us'),
    path('register', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout')
]

