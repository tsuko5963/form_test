from django.db import models

# Create your models here.

class PostModel(models.Model):
    name = models.CharField(max_length = 25)
    text = models.CharField(max_length = 25)

    def __str__(self):
        return self.name

class DogCatModel(models.Model):
    dog = models.BooleanField(default = False)
    cat = models.BooleanField(default = False)
