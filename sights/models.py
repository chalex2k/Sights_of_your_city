from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Landmark(models.Model):
    name = models.CharField(max_length=50)
    information = models.TextField()
    type = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    path_photos = models.CharField(max_length=100)

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name

    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('sights:landmark_detail', args=[self.name])