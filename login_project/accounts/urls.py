# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # Redirect homepage to login page
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
