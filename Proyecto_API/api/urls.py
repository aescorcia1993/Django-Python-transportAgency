from django.urls import path
from .views import PassengerView

urlpatterns = [
    path('passengers/', PassengerView.as_view(), name='passenger_list'),
    path('passengers/<int:id>', PassengerView.as_view(), name='passenger_process'),
    path('passengers/', PassengerView.as_view(), name='pass'),
]
