from django.db import models
from django.utils import timezone

# Create your models here.

class PostDogCatModel(models.Model):
    date = models.DateField(default=timezone.now)
    name = models.CharField(max_length = 25)
    text = models.CharField(max_length = 25)
    dog = models.BooleanField(default = False)
    cat = models.BooleanField(default = False)

    def __str__(self):
        return self.name
