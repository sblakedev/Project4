# from django.shortcuts import render
# from django.views import generic
# from .models import Booking

# # Create your views here.
# class BookingsList(generic.ListView):
#     model = Booking
#     queryset = Booking.objects.order_by('booking_date', 'booking_time')
#     template_name = 'bookings_list.html'
    
# def all_bookings(request):
#     bookings_list = Booking.objects.all()
#     return render(request, 'bookings_list.html' {'bookings_list': bookings_list})