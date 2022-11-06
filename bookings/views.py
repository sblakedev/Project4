from django.shortcuts import render, reverse
from django.views import generic
from django.views.generic.edit import FormView
from .models import Booking, CreateAccount
from .forms import BookingForm


# Create your views here.


def HomePage(request):
    """
    Renders Home Page View
    """
    return render(request, 'index.html')


class LogInPage(generic.DetailView):
    """
    Renders Log In Page View
    """

    def get(self, request):
        return render(request, 'log_in.html')


class BookPage(FormView):
    """
    Renders Booking Page View
    """
    template_name = 'book.html'
    form_class = BookingForm
    
    def booking_view(self, request):
        return render(request, 'book.html')
    
    def post(self, request):
        
        form = BookingForm(data=request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
        
        return render(request, 'index.html')


class MyBookings(generic.DetailView):
    """
    Renders My Booking Page View
    """
    template_name = "my_bookings.html"

    def get(self, request):
        return render(request, 'my_bookings.html')
