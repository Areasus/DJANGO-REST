from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=50)
    des = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Items(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    