from django.contrib import admin
from .models import Booking, CreateAccount


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    model = Booking
    list_display = ('name', 'email_address', 'phone')


@admin.register(CreateAccount)
class CreateAccountAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email_address', 'phone_number')
