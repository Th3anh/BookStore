from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView 

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/',views.login_view.as_view(), name="login"),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
]
    