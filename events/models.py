from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    cost = models.DecimalField(max_digits=6, decimal_places=2)

class Review(models.Model):
    user_profile = models.ForeignKey("accounts.UserProfile", on_delete=models.CASCADE, related_name='reviews')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    text = models.TextField()

    def __str__(self):
        return self.title