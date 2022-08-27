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
                passenger = passengers[0]
                datos = {'message': "Success", 'company': passenger}
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

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        try:
            Passenger.objects.create(name=jd['name'],
            lastName=jd['lastName'],
            dni=jd['dni'],
            address=jd['address'],
            phone1=jd['phone1'],
            gener=jd['gener'],
            country=jd['country'],
            state=jd['state'],
            email=jd['email'],
            dob=jd['dob'],
            status=jd['status'])

            datos = {'message': "Success"}
        except:
            datos = {'message': "Error saving passenger"}

        return JsonResponse(datos)
    
    def put(self, request, id):
        jd = json.loads(request.body)
        passengers = list(Passenger.objects.filter(id=id).values())
        if len(passengers) > 0:
            passenger = Passenger.objects.get(id=id)
            
            passenger.name = jd['name']
            passenger.lastName = jd['lastName']
            passenger.dni = jd['dni']
            passenger.address = jd['address']
            passenger.phone1 = jd['phone1']
            passenger.gener = jd['gener']
            passenger.country = jd['country']
            passenger.state = jd['state']
            passenger.email = jd['email']
            passenger.dob = jd['dob']
            passenger.status = jd['status']

            passenger.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Passenger not found..."}
        return JsonResponse(datos)
    
    def delete(self, request, id):
        passengers = list(Passenger.objects.filter(id=id).values())
        if len(passengers) > 0:
            Passenger.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Passenger not found..."}
        return JsonResponse(datos)