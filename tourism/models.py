from django.db import models
from django.db import models

class Beach(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    activities = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Review(models.Model):
    beach = models.ForeignKey(Beach, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.user_name
# Create your models here.
