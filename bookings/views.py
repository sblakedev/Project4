from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from django.views import generic, View
from django.views.generic.edit import FormView
from .models import Booking
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
        form = BookingForm(request.POST, request.FILES)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, 'Booking is confirmed')
            return redirect('my_bookings')
        else:
            messages.error(
                request, 'Invalid, incorrect info or double booking')

    form = BookingForm()
    context = {
        'form': form
    }

    return render(request, 'book.html', context)


def my_bookings(request):
    """
    Renders My Booking Page View
    """
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(user=request.user)
        context = {
            'bookings': bookings
        }

        return render(request, 'my_bookings.html', context)

    else:
        return redirect('../accounts/signup')

    
def edit_bookings(request):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            booking.save()
            messages.success(request, 'Your booking has been updated')
            return redirect('my_bookings')
        else:
            messages.error(
                request, 'Invalid, incorrect info or double booking')

    form = BookingForm(instance=booking)
    context = {
        'form': form
    }

    return render(request, 'edit_booking.html', context)