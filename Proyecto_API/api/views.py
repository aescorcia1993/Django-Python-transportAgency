from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Bus, Driver, Passenger, Seats, Trip
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
            drivers = list(Driver.objects.filter(bus_id=id).values())
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

class TripView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            trips = list(Trip.objects.filter(id=id).values())
            if len(trips) > 0:
                trip = trips[0]
                datos = {'message': "Success", 'trip': trip}
            else:
                datos = {'message': "trips not found..."}
            return JsonResponse(datos)
        else:
            trips = list(Trip.objects.values())
            if len(trips) > 0:
                datos = {'message': "Success", 'trips': trips}
            else:
                datos = {'message': "trips not found..."}
            return JsonResponse(datos)

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        try:
            Trip.objects.create(routeName=jd['routeName'],
            description=jd['description'],
            arriveTime=jd['arriveTime'],
            departureTime=jd['departureTime'],
            status=jd['status'])

            datos = {'message': "Success"}
        except:
            datos = {'message': "Error saving trip"}

        return JsonResponse(datos)
    
    def put(self, request, id):
        jd = json.loads(request.body)
        trips = list(Trip.objects.filter(id=id).values())
        if len(trips) > 0:
            trip = Trip.objects.get(id=id)

            trip.routeName=jd['routeName']
            trip.description=jd['description']
            trip.arriveTime=jd['arriveTime']
            trip.departureTime=jd['departureTime']
            trip.status = jd['status']

            trip.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Trip not found..."}
        return JsonResponse(datos)
    
    def delete(self, request, id):
        trips = list(Trip.objects.filter(id=id).values())
        if len(trips) > 0:
            Trip.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Trip not found..."}
        return JsonResponse(datos)

class SeatsView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            seatses = list(Seats.objects.filter(trip_id=id).values())
            if len(seatses) > 0:
                seats = seatses[0]
                datos = {'message': "Success", 'seats': seats}
            else:
                datos = {'message': "seats not found..."}
            return JsonResponse(datos)
        else:
            seatses = list(Seats.objects.values())
            if len(seatses) > 0:
                datos = {'message': "Success", 'seats': seatses}
            else:
                datos = {'message': "seats not found..."}
            return JsonResponse(datos)

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        global tripa
        tripa = Trip()
        tripas = list(Trip.objects.filter(id=jd['trip_id']).values())

        global busa
        busa = Bus()
        buses = list(Bus.objects.filter(id=jd['bus_id']).values())

        if len(tripas) > 0:
                tripa = Trip.objects.get(id=jd['trip_id'])

        if len(buses) > 0:
                busa = Bus.objects.get(id=jd['bus_id'])    
        
        try:
            Seats.objects.create(
            trip= tripa,
            bus = busa,
            seat1 = Passenger.objects.get(id=jd['seat1']) if jd['seat1'] != None else  None,
            seat2 = Passenger.objects.get(id=jd['seat2']) if jd['seat2'] != None else  None,
            seat3 = Passenger.objects.get(id=jd['seat3']) if jd['seat3'] != None else  None,
            seat4 = Passenger.objects.get(id=jd['seat4']) if jd['seat4'] != None else  None,
            seat5 = Passenger.objects.get(id=jd['seat5']) if jd['seat5'] != None else  None,
            seat6 = Passenger.objects.get(id=jd['seat6']) if jd['seat6'] != None else  None,
            seat7 = Passenger.objects.get(id=jd['seat7']) if jd['seat7'] != None else  None,
            seat8 = Passenger.objects.get(id=jd['seat8']) if jd['seat8'] != None else  None,
            seat9 = Passenger.objects.get(id=jd['seat9']) if jd['seat9'] != None else  None,
            seat10 = Passenger.objects.get(id=jd['seat10']) if jd['seat10'] != None else  None,
            )

            datos = {'message': "Success"}
        except Exception as err:
            print("ERROR: ",err)
            datos = {'message': "Error saving seats"}

        return JsonResponse(datos)
    
    def put(self, request, id):
        
        jd = json.loads(request.body)
        seatses = list(Seats.objects.filter(id=id).values())
        if len(seatses) > 0:
           seats = Seats.objects.get(id=id)
           seats.seat1 = Passenger.objects.get(id=jd['seat1']) if jd['seat1'] != None else  None
           seats.seat2 = Passenger.objects.get(id=jd['seat2']) if jd['seat2'] != None else  None
           seats.seat3 = Passenger.objects.get(id=jd['seat3']) if jd['seat3'] != None else  None
           seats.seat4 = Passenger.objects.get(id=jd['seat4']) if jd['seat4'] != None else  None
           seats.seat5 = Passenger.objects.get(id=jd['seat5']) if jd['seat5'] != None else  None
           seats.seat6 = Passenger.objects.get(id=jd['seat6']) if jd['seat6'] != None else  None
           seats.seat7 = Passenger.objects.get(id=jd['seat7']) if jd['seat7'] != None else  None
           seats.seat8 = Passenger.objects.get(id=jd['seat8']) if jd['seat8'] != None else  None
           seats.seat9 = Passenger.objects.get(id=jd['seat9']) if jd['seat9'] != None else  None
           seats.seat10 = Passenger.objects.get(id=jd['seat10']) if jd['seat10'] != None else  None
           
           seats.save()
           datos = {'message': "Success"}
        else:
            datos = {'message': "Seats not found..."}
        return JsonResponse(datos)
    
    def delete(self, request, id):
        seatses = list(Seats.objects.filter(id=id).values())
        if len(seatses) > 0:
            Seats.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Seats not found..."}
        return JsonResponse(datos)
