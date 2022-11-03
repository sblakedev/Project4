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


class MenuPage(generic.DetailView):
    """
    Renders Menu Page View
    """

    def get(self, request):
        return render(Request, 'menu.html')


class ContactPage(generic.DetailView):
    """
    Renders Contact Page View
    """

    def get(self, request):
        return render(Request, 'contact.html')


class LogInPage(generic.DetailView):
    """
    Renders Log In Page View
    """

    def get(self, request):
        return render(Request, 'log_in.html')


class BookPage(ListView):
    """
    Renders Booking Page View
    """
    model = Booking
    queryset = Booking.objects.all()
    template_name = 'book.html'

    def get(self, request):
        return render(Request, 'book.html')
