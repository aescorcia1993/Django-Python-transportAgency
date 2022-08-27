from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Passenger
import json

# Create your views here.

class PassengerView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            passengers = list(Passenger.objects.filter(id=id).values())
            if len(passengers) > 0:
                company = passengers[0]
                datos = {'message': "Success", 'company': company}
            else:
                datos = {'message': "passengers not found..."}
            return JsonResponse(datos)
        else:
            passengers = list(Passenger.objects.values())
            if len(passengers) > 0:
                datos = {'message': "Success", 'passengers': passengers}
            else:
                datos = {'message': "passengers not found..."}
            return JsonResponse(datos)

