from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('', views.BookPage.as_view(), name='book'),
    path('', views.my_bookings.as_view(), name='my_bookings'),
]
