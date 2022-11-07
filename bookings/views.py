from django.shortcuts import render, reverse
from django.views import generic, View
from django.views.generic.edit import FormView
from .models import Booking, CreateAccount
from .forms import BookingForm


# Create your views here.


def home(request):
    """
    Renders Home Page View
    """

    return render(request, 'index.html')


def BookPage(request):
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

        return render(request, 'my_bookings.html')


class MyBookings(generic.DetailView):
    """
    Renders My Booking Page View
    """
    template_name = "my_bookings.html"

    def get(self, request):
        return render(request, 'my_bookings.html')
