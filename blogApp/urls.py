from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="Home_Page"),
    path('about/', views.about, name="about_Page")
]
