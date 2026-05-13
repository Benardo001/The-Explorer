from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Beach(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    activities = models.TextField(blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='beach_images/', blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    beach = models.ForeignKey(Beach, on_delete=models.CASCADE, related_name='bookings')
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.beach.name} booking by {self.user.username}"


class Review(models.Model):
    beach = models.ForeignKey(Beach, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField()
    rating = models.IntegerField(default=5)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        username = self.user.username if self.user else 'Anonymous'
        return f"{username} ({self.rating})"
