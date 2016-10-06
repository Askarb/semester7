from django.db import models


class Books(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    count = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    book_id = models.IntegerField()
    date = models.DateField()

