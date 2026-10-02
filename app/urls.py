from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('health', views.health, name="health"),
    path('healthz', views.health, name="healthz"),
    path('galery', views.galery, name="galery"),
    path('about', views.About, name="about"),
    path('product/<int:product_id>/', views.product_detail, name="product_detail"),
    path('checkout/<int:product_id>/', views.checkout, name="checkout"),
    #rutas de login, logout, password reset, etc
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

]