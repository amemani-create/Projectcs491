from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact.html', views.contact, name="contact"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('portfolio-single/', views.portfolio_single, name="portfolio_single"),
    path('service/', views.service, name="service"),

]
