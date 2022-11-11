from django.shortcuts import render, reverse, redirect, get_object_or_404
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
    Renders Booking Page View.
    This contains the booking form. If the form is valid,
    the user will see a success message and will be redirected
    to the My Bookings page. If the form is not valid, users
    will see an error message.
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_form = form.save(commit=False)
            booking_form.user = request.user
            booking_form.save()
            messages.success(request, 'Booking is confirmed')
            return redirect('my_bookings')
        else:
            messages.error(
                request, 'Invalid, incorrect info or double booking')
            print(form.errors)

    form = BookingForm()
    context = {
        'form': form
    }

    return render(request, 'book.html', context)


def my_bookings(request):
    """
    Renders My Booking Page View. This
    page shows all of the user's current
    bookings.
    """
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(user=request.user)
        context = {
            'bookings': bookings
        }

        return render(request, 'my_bookings.html', context)

    else:
        return redirect('../accounts/signup')


def edit_bookings(request, booking_id):
    """
    When the user clicks the edit button under
    their booking, they will be brought to a 
    new page where they can edit their booking.
    When they submit their changes, they will be
    redirected to the My Bookings page
    """
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
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


def delete_booking(request, booking_id):
    """
    When the user clicks the delete button under
    their booking, they will see a message confirming
    the deletion.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    # 
    messages.success(request, 'Your booking has been cancelled')
    return redirect('/')
