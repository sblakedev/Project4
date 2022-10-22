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


OCCASION = (
    ('Birthday', 'BIRTHDAY'),
    ('Anniversary', 'ANNIVERSARY'),
    ('Date', 'DATE'),
    ('Business Dinner', 'BUSINESS'),
    ('Hen Party', 'HEN'),
    ('Stag Party', 'STAG'),
    
)

# Create your models here.
  
class Booking(models.Model):
    Booking_Date =
    Booking_Time = 
    No_of_guests =
    Booking_event = 