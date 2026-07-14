from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('galery', views.Galery, name="galery"),
    path('about', views.About, name="about"),
    #rutas de login, logout, password reset, etc
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

]