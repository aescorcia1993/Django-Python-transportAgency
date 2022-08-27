from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Bus, Driver, Passenger
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

class DriverView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            drivers = list(Driver.objects.filter(id=id).values())
            if len(drivers) > 0:
                driver = drivers[0]
                datos = {'message': "Success", 'company': driver}
            else:
                datos = {'message': "drivers not found..."}
            return JsonResponse(datos)
        else:
            drivers = list(Driver.objects.values())
            if len(drivers) > 0:
                datos = {'message': "Success", 'drivers': drivers}
            else:
                datos = {'message': "drivers not found..."}
            return JsonResponse(datos)

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        global busa
        busa = Bus()
        # print(jd)
        #try:
        buses = list(Bus.objects.filter(placa=jd['placa']).values())
            
        if len(buses)> 0:
                busa = Bus.objects.get(placa=jd['placa'])
        else:
                Bus.objects.create(
                    placa=jd["placa"], 
                    modelo="",
                    codigo="",
                    motor ="",
                    chasis="",
                    status="A",
                )

        Driver.objects.create(
            bus=  busa, 
            name=jd['name'],
            lastName=jd['lastName'],
            dni=jd['dni'],
            dob=jd['dob'],
            address=jd['address'],
            phone1=jd['phone1'],
            phone2=jd['phone2'],
            gener=jd['gener'],
            license=jd['license'],
            country=jd['country'],
            state=jd['state'],
            email=jd['email'],
            status=jd['status'])

        datos = {'message': "Success"}
        #except:
            #datos = {'message': "Error saving driver"}

        return JsonResponse(datos)
    
    def put(self, request, id):
        jd = json.loads(request.body)
        drivers = list(Driver.objects.filter(bus_id=id).values())
        if len(drivers) > 0:
            driver = Driver.objects.get(bus_id=id)

            driver.name = jd['name']
            driver.lastName = jd['lastName']
            driver.dni = jd['dni']
            driver.dob = jd['dob']
            driver.address = jd['address']
            driver.phone1 = jd['phone1']
            driver.phone2 = jd['phone2']
            driver.gener = jd['gener']
            driver.license = jd['license']
            driver.country = jd['country']
            driver.state = jd['state']
            driver.email = jd['email']
            driver.status = jd['status']

            driver.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Driver not found..."}
        return JsonResponse(datos)
    
    def delete(self, request, id):        
        drivers = list(Driver.objects.filter(bus_id=id).values())
        if len(drivers) > 0:
            Driver.objects.filter(bus_id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Driver not found..."}
        return JsonResponse(datos)

class BusView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            buses = list(Bus.objects.filter(id=id).values())
            if len(buses) > 0:
                bus = buses[0]
                datos = {'message': "Success", 'company': bus}
            else:
                datos = {'message': "buses not found..."}
            return JsonResponse(datos)
        else:
            buses = list(Bus.objects.values())
            if len(buses) > 0:
                datos = {'message': "Success", 'buses': buses}
            else:
                datos = {'message': "buses not found..."}
            return JsonResponse(datos)

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        try:
            Bus.objects.create(placa=jd['placa'],
            modelo=jd['modelo'],
            codigo=jd['codigo'],
            motor=jd['motor'],
            chasis=jd['chasis'],
            status=jd['status'])

            datos = {'message': "Success"}
        except:
            datos = {'message': "Error saving bus"}

        return JsonResponse(datos)
    
    def put(self, request, id):
        jd = json.loads(request.body)
        buses = list(Bus.objects.filter(id=id).values())
        if len(buses) > 0:
            bus = Bus.objects.get(id=id)


            bus.placa=jd['placa']
            bus.modelo=jd['modelo']
            bus.codigo=jd['codigo']
            bus.motor=jd['motor']
            bus.chasis=jd['chasis']
            bus.status = jd['status']

            bus.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Bus not found..."}
        return JsonResponse(datos)
    
    def delete(self, request, id):
        buses = list(Bus.objects.filter(id=id).values())
        if len(buses) > 0:
            Bus.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Bus not found..."}
        return JsonResponse(datos)
