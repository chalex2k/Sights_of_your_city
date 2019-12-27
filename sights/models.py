from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from account.models import Profile


class Landmark(models.Model):
    name = models.CharField(max_length=100)
    information = models.TextField()
    type = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='landmarks')
    comment = models.TextField()
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name

    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('sights:landmark_detail', args=[self.name])


class Comment(models.Model):
    landmark = models.ForeignKey(Landmark, on_delete=models.CASCADE, related_name='comments')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
    body = models.CharField(max_length=500)
    created = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
         ordering = ('created',)

    def __str__(self):
        return 'Comment  by ... on{}'.format(self.landmark)


class Photo(models.Model):
    image = models.ImageField(upload_to='photos')
    landmark = models.ForeignKey(Landmark, on_delete=models.CASCADE, related_name='photos')
