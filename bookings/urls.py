from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('', views.BookPage.as_view(), name='book'),
    path('', views.AboutPage.as_view(), name='about'),
    path('', views.MenuPage.as_view(), name='menu'),
]
