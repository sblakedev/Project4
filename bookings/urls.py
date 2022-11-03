from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage.as_view(), name='home.html'),
    path('', views.BookPage.as_view(), name='book.html'),
    path('', views.AboutPage.as_view(), name='about.html'),
    path('', views.MenuPage.as_view(), name='menu.html'),
]
