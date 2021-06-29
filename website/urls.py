from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact.html', views.contact, name="contact"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('portfolio-single/<int:id>/<slug:slug>/', views.portfolio_single, name="portfolio_single"),
    path('consult/', views.consult, name="consult"),
    path('trees/', views.tree_profile, name="tree_profile"),
    path('tree-single/<int:id>/<slug:slug>/', views.tree_single, name="tree_single"),

]
