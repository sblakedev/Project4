from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.book_page, name='book'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
    path('edit_booking/<booking_id>', views.edit_bookings, name='edit_bookings'),
    path('delete_booking/<booking_id>', views.delete_booking, name='delete_bookings'),
]
