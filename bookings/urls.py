from . import views
from django.urls import path


urlpatterns = [
    path('', views.BookPage.as_view(), name='book')
]
