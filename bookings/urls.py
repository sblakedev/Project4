from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage, name='home'),
    path('BookPage', views.BookPage, name='book'),
]
