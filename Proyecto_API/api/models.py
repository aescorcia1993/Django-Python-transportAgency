from datetime import datetime
from pickle import FALSE, TRUE
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
    country = models.CharField(max_length=20, default="")
    state = models.CharField(max_length=20, default="")
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
    status = models.CharField(max_length=10, default="A")

class Trip(models.Model):
    routeName = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    arriveTime = models.DateTimeField(null=True, blank=True)
    departureTime = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=1, default="A")

class Seats(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, null=True)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True)
    seat1 = models.ForeignKey(Passenger, related_name='seat1', on_delete=models.SET_NULL, null=True)
    seat2 = models.ForeignKey(Passenger,related_name='seat2', on_delete=models.SET_NULL, null=True)
    seat3 = models.ForeignKey(Passenger,related_name='seat3', on_delete=models.SET_NULL, null=True)
    seat4 = models.ForeignKey(Passenger,related_name='seat4', on_delete=models.SET_NULL, null=True)
    seat5 = models.ForeignKey(Passenger,related_name='seat5', on_delete=models.SET_NULL, null=True)
    seat6 = models.ForeignKey(Passenger,related_name='seat6', on_delete=models.SET_NULL, null=True)
    seat7 = models.ForeignKey(Passenger,related_name='seat7', on_delete=models.SET_NULL, null=True)
    seat8 = models.ForeignKey(Passenger,related_name='seat8', on_delete=models.SET_NULL, null=True)
    seat9 = models.ForeignKey(Passenger,related_name='seat9', on_delete=models.SET_NULL, null=True)
    seat10 = models.ForeignKey(Passenger,related_name='seat10', on_delete=models.SET_NULL, null=True)
    
class Book(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, null=True)
    seats = models.ForeignKey(Seats, on_delete=models.CASCADE, null=True)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, null=True)
    #createAt = models.DateTimeField(auto_now_add=datetime.now())
    description = models.CharField(max_length=50, null=True)
  