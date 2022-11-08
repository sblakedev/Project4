from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    model = Booking
    list_display = ('name', 'email_address', 'phone', 'booking_date',
                    'booking_time', 'no_of_guests', 'booking_event')
    list_filter = ('name', 'booking_date')
    search_fields = ['name', 'email_address', 'phone']
