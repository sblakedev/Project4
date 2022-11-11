from django import forms
from django.forms import ModelForm
from django.forms.widgets import DateInput
from .models import CreateAccount, Booking


class DateInput(forms.DateInput):

    input_type = 'date'


class TimePickerInput(forms.TimeInput):

    input_type = 'time'


class BookingForm(forms.ModelForm):
    name = forms.CharField(
        label='Name',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Name'})
    )

    email_address = forms.EmailField(
        label='Email Address',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Email Address'}),
    )

    phone = forms.CharField(
        label='Phone Number',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}),
    )
    
    class Meta:
        model = Booking

        exclude = ('user', )
        widgets = {
            'booking_date': DateInput(),
        }
