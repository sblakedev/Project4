from django.shortcuts import render, reverse
from django.views import generic
from .models import Booking, CreateAccount


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


def BookPage(request):
    """
    Renders Booking Page View
    """

    return render(request, 'book.html')


class MyBookings(generic.DetailView):
    """
    Renders My Booking Page View
    """
    template_name = "my_bookings.html"

    def get(self, request):
        return render(request, 'my_bookings.html')
