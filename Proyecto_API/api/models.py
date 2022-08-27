from django.db import models

# Create your models here.

class UserAgency(models.Model):
    userName = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=50, default="")
    status = models.CharField(max_length=1, default="A")

class Passenger(models.Model):
    name = models.CharField(max_length=50, default="")
    lastName = models.CharField(max_length=50, default="")
    dni = models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=50, default="")
    phone1 = models.CharField(max_length=10, default="")
    gener = models.CharField(max_length=2, default="")
    country = models.CharField(max_length=10, default="")
    state = models.CharField(max_length=10, default="")
    email = models.CharField(max_length=30, default="")
    dob = models.CharField(max_length=50, default="")
    status = models.CharField(max_length=1, default="A")

class Bus(models.Model):
    placa = models.CharField(max_length=6, default="")
    modelo = models.CharField(max_length=6)
    codigo = models.CharField(max_length=6)
    motor = models.CharField(max_length=30)
    chasis = models.CharField(max_length=30) 
    status = models.CharField(max_length=1, default="A")

class Driver(models.Model):
    bus = models.OneToOneField(
        Bus,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    name = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    dni = models.PositiveIntegerField()
    dob = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone1 = models.CharField(max_length=10)
    phone2 = models.CharField(max_length=10)
    gener = models.CharField(max_length=1)
    license = models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    email = models.EmailField()
    #status = models.BooleanField()

class Trip(models.Model):
    routeName = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    #arriveTime = models.DateTimeField(default={})
    #departureTime = models.DateTimeField(default={})
    status = models.CharField(max_length=1, default="A")

class Seats(models.Model):
    trip = models.OneToOneField(
        Trip,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    seat1 = models.CharField(max_length=50)
    seat2 = models.CharField(max_length=50)
    seat3 = models.CharField(max_length=50)
    seat4 = models.CharField(max_length=50)
    seat5 = models.CharField(max_length=50)
    seat6 = models.CharField(max_length=50)
    seat7 = models.CharField(max_length=50)
    seat8 = models.CharField(max_length=50)
    seat9 = models.CharField(max_length=50)
    seat10 = models.CharField(max_length=50)
    
class Book(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    seats = models.OneToOneField(
        Seats,
        on_delete=models.CASCADE,
        primary_key=True,
    )    