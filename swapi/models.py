from django.db import models

# Create your models here.
class Human(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=1024)
    gender = models.IntegerField()
    height = models.IntegerField()
    birth_year = models.CharField(max_length=1024)
    mass = models.IntegerField()
    home_planet = models.CharField(max_length=1024)

    def __str__(self):
        return self.name
