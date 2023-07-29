from django.db import models

# Create your models here.

class PostDogCatModel(models.Model):
    name = models.CharField(max_length = 25)
    text = models.CharField(max_length = 25)
    dog = models.BooleanField(default = False)
    cat = models.BooleanField(default = False)

    def __str__(self):
        return self.name
