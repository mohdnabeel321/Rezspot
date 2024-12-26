from django.db import models
from django.contrib.auth.models import User

class Reservation(models.Model):
    CUISINE_CHOICES = [
        ('italian', 'Italian'),
        ('chinese', 'Chinese'),
        ('indian', 'Indian'),
        ('mexican', 'Mexican'),
        ('japanese', 'Japanese'),
        ('thai', 'Thai'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reservations")
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    number_of_seats = models.IntegerField()
    cuisine = models.CharField(max_length=100, choices=CUISINE_CHOICES, blank=True)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Reservation for {self.name} on {self.reservation_date} at {self.reservation_time}"
