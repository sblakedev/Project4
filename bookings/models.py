from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Options for bookings

TIME = (
    ('17:00', '17:00'),
    ('17:30', '17:30'),
    ('18:00', '18:00'),
    ('18:30', '18:30'),
    ('19:00', '19:00'),
    ('19:30', '19:30'),
    ('20:00', '20:00'),
    ('20:30', '20:30'),
    ('21:00', '21:00'),
    ('21:30', '21:30'),
    ('22:00', '22:00'),

)


NO_OF_GUESTS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),

)


EVENT = (
    ('BIRTHDAY', 'Birthday'),
    ('ANNIVERSARY', 'Anniversary'),
    ('DATE', 'Date'),
    ('BUSINESS', 'Business Dinner'),
    ('HEN', 'Hen Party'),
    ('STAG', 'Stag Party'),
    ('NONE', 'None'),

)


TITLE = (
    ('MS', 'Ms'),
    ('MISS', 'Miss'),
    ('MRS', 'Mrs'),
    ('MR', 'Mr'),
    ('NONE', '--'),

)

# Create your models here.


class Booking(models.Model):
    guest = models.ForeignKey(User, on_delete=models.CASCADE, related_name="guest_bookings")
    name = models.CharField(max_length=50, null=True, blank=False)
    email_address = models.EmailField(null=True, blank=True),
    phone = models.IntegerField(null=True, blank=False)
    booking_date = models.DateField(auto_now=True, blank=False)
    booking_time = models.TimeField(auto_now=True, choices=TIME, blank=False)
    no_of_guests = models.CharField(max_length=2, choices=NO_OF_GUESTS, blank=False)
    booking_event = models.CharField(max_length=50, choices=EVENT, blank=False)

    def __str__(self):
        return self.name

class CreateAccount(models.Model):
    title = models.CharField(max_length=4, blank=False)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email_address = models.EmailField(blank=True)
    phone_number = models.IntegerField(blank=False)