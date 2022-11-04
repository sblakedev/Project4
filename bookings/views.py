from django.shortcuts import render
from django.views import generic
from .models import Booking, CreateAccount


# Create your views here.


class HomePage(generic.DetailView):
    """
    Renders Home Page View
    """

    template_name = "index.html"

    def get(self, request):
        return render(request, 'index.html')


class LogInPage(generic.DetailView):
    """
    Renders Log In Page View
    """

    def get(self, request):
        return render(request, 'log_in.html')


class BookPage(generic.DetailView):
    """
    Renders Booking Page View
    """
    model = Booking
    queryset = Booking.objects.all()
    template_name = 'book.html'

    def get(self, request):
        return render(request, 'book.html')
