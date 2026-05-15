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


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Contact from {self.name}: {self.subject}"


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.IntegerField(default=5)
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        username = self.user.username if self.user else 'Guest'
        return f"Feedback from {username} ({self.rating})"


class TouristAttraction(models.Model):
    CATEGORY_CHOICES = [
        ('national_park', 'National Park'),
        ('wildlife', 'Wildlife Reserve'),
        ('cultural', 'Cultural Site'),
        ('mountain', 'Mountain'),
        ('waterfall', 'Waterfall'),
        ('island', 'Island'),
        ('historical', 'Historical Site'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    entry_fee = models.IntegerField(default=0)
    best_time_to_visit = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='attraction_images/', blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Accommodation(models.Model):
    ACCOMMODATION_TYPE_CHOICES = [
        ('hotel', 'Hotel'),
        ('resort', 'Resort'),
        ('guesthouse', 'Guesthouse'),
        ('apartment', 'Apartment'),
        ('villa', 'Villa'),
        ('cottage', 'Cottage'),
        ('camp', 'Camp'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    accommodation_type = models.CharField(max_length=20, choices=ACCOMMODATION_TYPE_CHOICES)
    description = models.TextField()
    price_per_night = models.IntegerField()
    max_guests = models.IntegerField(default=2)
    amenities = models.TextField(blank=True, help_text="Comma-separated list of amenities")
    image = models.ImageField(upload_to='accommodation_images/', blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    contact_info = models.CharField(max_length=200, blank=True)
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_amenities_list(self):
        """Return amenities as a list"""
        if self.amenities:
            return [amenity.strip() for amenity in self.amenities.split(',')]
        return []


class Transport(models.Model):
    TRANSPORT_TYPE_CHOICES = [
        ('bus', 'Bus'),
        ('matatu', 'Matatu'),
        ('taxi', 'Taxi'),
        ('car_rental', 'Car Rental'),
        ('motorcycle', 'Motorcycle'),
        ('bicycle', 'Bicycle'),
        ('boat', 'Boat'),
        ('ferry', 'Ferry'),
        ('train', 'Train'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    transport_type = models.CharField(max_length=20, choices=TRANSPORT_TYPE_CHOICES)
    description = models.TextField()
    location = models.CharField(max_length=100, help_text="Base location or route")
    destination = models.CharField(max_length=100, blank=True, help_text="If applicable")
    price_per_trip = models.IntegerField(help_text="Price per trip or per hour")
    price_unit = models.CharField(max_length=20, default="trip", help_text="e.g., trip, hour, day")
    capacity = models.IntegerField(default=1, help_text="Number of passengers")
    amenities = models.TextField(blank=True, help_text="Comma-separated list of amenities")
    image = models.ImageField(upload_to='transport_images/', blank=True, null=True)
    contact_info = models.CharField(max_length=200, blank=True)
    website = models.URLField(blank=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    available_24_7 = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} ({self.get_transport_type_display()})"

    def get_amenities_list(self):
        """Return amenities as a list"""
        if self.amenities:
            return [amenity.strip() for amenity in self.amenities.split(',')]
        return []
