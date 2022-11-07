from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.book_page, name='book'),
]
