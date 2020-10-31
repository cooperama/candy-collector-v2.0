from django.urls import path
from . import views


urlpatterns = [
    # Static
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]