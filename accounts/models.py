from django.db import models
from django.contrib.auth.models import User
from events.models import Event

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile" )
    attending = models.ManyToManyField(
        Event, blank=True, related_name='attending')
    
    def __str__(self):
        return self.user.username


