from django.db import models
from django.urls import reverse

from accounts.models import CustomUser

# Create your models here.

class Snack(models.Model):
    name = models.CharField(max_length=256)
    purchaser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('snack_list.html')