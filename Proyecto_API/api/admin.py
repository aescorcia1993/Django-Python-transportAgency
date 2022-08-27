from django.contrib import admin
from .models import Book, Bus, Driver, Passenger, Seats, Trip, UserAgency

# Register your models here.

admin.site.register(UserAgency)
admin.site.register(Passenger)
admin.site.register(Bus)
admin.site.register(Driver)
admin.site.register(Trip)
admin.site.register(Seats)
admin.site.register(Book)