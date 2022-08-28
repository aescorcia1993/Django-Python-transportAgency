from django.urls import path
from .views import BusView, DriverView, PassengerView, ReportView, SeatsView, TripView, BookView

urlpatterns = [
    path('passengers', PassengerView.as_view(), name='passenger_list'),
    path('passengers/<int:id>', PassengerView.as_view(), name='passenger_process'),

    path('drivers', DriverView.as_view(), name='driver_list'),
    path('drivers/<int:id>', DriverView.as_view(), name='driver_process'),

    path('buses', BusView.as_view(), name='bus_list'),
    path('buses/<int:id>', BusView.as_view(), name='bus_process'),
    
    path('trips', TripView.as_view(), name='trip_list'),
    path('trips/<int:id>', TripView.as_view(), name='trip_process'),

    path('seats', SeatsView.as_view(), name='seat_list'),
    path('seats/<int:id>', SeatsView.as_view(), name='seat_process'),

    path('books', BookView.as_view(), name='book_list'),
    path('books/<int:id>', BookView.as_view(), name='book_process'),

    path('tripsByAvg', ReportView.as_view(), name='report1'),
    path('busBySoldTickets/<int:capacity>', ReportView.as_view(), name='report2'),
]
