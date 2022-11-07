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


def book_page(request):
    """
    Renders Booking Page View
    """
    if request.method == 'POST':
        form = BookingForm(data=request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('my_bookings')

    form = BookingForm()
    context = {
        'form': BookingForm
    }

    return render(request, 'book.html')


def my_bookings(request):
    """
    Renders My Booking Page View
    """
    template_name = "my_bookings.html"

    def get(self, request):
        return render(request, 'my_bookings.html')
