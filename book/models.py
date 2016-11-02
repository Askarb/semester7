from django.db import models


class Books(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    count = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    book_id = models.ForeignKey(Books)
    date = models.DateField()


class Teams(models.Model):
    name = models.CharField(max_length=50)
    coach = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    position = models.CharField(max_length=50)
    team_id = models.ForeignKey(Teams)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    cources = models.ManyToManyField(Course)

    def __str__(self):
        return self.name


class Phone(models.Model):
    model = models.CharField(max_length=50)
    company = models.CharField(max_length=50)

