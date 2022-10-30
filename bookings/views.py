from django.shortcuts import render
from django.views import generic


# Create your views here.

# Home Page
"""Home Page View"""
class HomePage(generic.DetailView):
    template_name = "index.html"
    
    def get(self, request):
        return render(request, 'index.html')

# Menu Page
"""Menu Page View"""
class MenuPage(View)

# Book a Table Page
"""Book a Table Page View"
class Booking


class BookingsList(generic.ListView):
    model = Booking
    queryset = Booking.objects.order_by('booking_date', 'booking_time')
    template_name = 'bookings_list.html'
    
def all_bookings(request):
    bookings_list = Booking.objects.all()
    return render(request, 'bookings_list.html' {'bookings_list': bookings_list})