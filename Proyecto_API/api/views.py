import math
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.db.models import F, Sum, Avg
from django.db import connection
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from .models import Book, Bus, Driver, Passenger, Seats, Trip
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
                datos = {'message': "Success", 'passengers': passenger}
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

class BookView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            books = list(Book.objects.filter(id=id).values())
            if len(books) > 0:
                books = books[0]
                datos = {'message': "Success", 'books': books}
            else:
                datos = {'message': "books not found..."}
            return JsonResponse(datos)
        else:
            books = list(Book.objects.values())
            if len(books) > 0:
                datos = {'message': "Success", 'books': books}
            else:
                datos = {'message': "books not found..."}
            return JsonResponse(datos)

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        global tripa
        tripa = Trip()
        tripas = list(Trip.objects.filter(id=jd['trip_id']).values())
        
        global busa
        seatsa = Seats()
        seatsas = list(Seats.objects.filter(id=jd['seats_id']).values())

        global passengera
        passengera = Passenger()
        passengers = list(Passenger.objects.filter(id=jd['passenger_id']).values())

        if len(tripas) > 0:
                tripa = Trip.objects.get(id=jd['trip_id'])

        if len(seatsas) > 0:
                seatsa = Seats.objects.get(id=jd['seats_id'])    
        
        if len(passengers) > 0:
                passengera = Passenger.objects.get(id=jd['passenger_id'])
        
        try:

            global pos
            seatField = 'seat'+ str(jd['position'])
            
            if jd['position'] < 10 and jd['position'] > 0:
                 pos = jd['position'] 
            else:
                 print("Position must be 1 to 10.")
                 raise ValueError("Position must be 1 to 10")
            
            
            if pos == 1 and seatsa.seat1 == None:
                seatsa.seat1 = passengera
            elif pos == 2 and seatsa.seat2 == None:
                seatsa.seat2 = passengera    
            elif pos == 3 and seatsa.seat3 == None:
                seatsa.seat3 = passengera 
            elif pos == 4 and seatsa.seat4 == None:
                seatsa.seat4 = passengera 
            elif pos == 5 and seatsa.seat5 == None:
                seatsa.seat5 = passengera 
            elif pos == 6 and seatsa.seat6 == None:
                seatsa.seat6 = passengera 
            elif pos == 7 and seatsa.seat7 == None:
                seatsa.seat7 = passengera 
            elif pos == 8 and seatsa.seat8 == None:
                seatsa.seat8 = passengera         
            elif pos == 9 and seatsa.seat9 == None:
                seatsa.seat9 = passengera 
            elif pos == 10 and seatsa.seat10 == None:
                seatsa.seat10 = passengera 

            else:
                print("Position already sold")
                raise ValueError("Position already sold")

            seatsa.save()

            Book.objects.create(
            trip= tripa,
            seats = seatsa,
            passenger = passengera,
            description = jd['description'],
            position = pos)

            datos = {'message': "Success"}
        except Exception as err:
            print("ERROR: ",err)
            datos = {'message': "Error saving seats. " + err.args[0]}

        return JsonResponse(datos)
    
    def delete(self, request, id):
        seatses = list(Seats.objects.filter(id=id).values())
        if len(seatses) > 0:
            Seats.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Seats not found..."}
        return JsonResponse(datos)

class ReportView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
 

    def get(self, request, id=0):
            sqlQ =   '''SELECT id, trip_id, AVG((CASE WHEN seat1_id IS NOT NULL THEN 1 ELSE 0 END) 
            + (CASE WHEN seat2_id IS NOT NULL THEN 1 ELSE 0 END) 
            + (CASE WHEN seat3_id IS NOT NULL THEN 1 ELSE 0 END) 
            + (CASE WHEN seat4_id IS NOT NULL THEN 1 ELSE 0 END) 
            + (CASE WHEN seat5_id IS NOT NULL THEN 1 ELSE 0 END) 
            + (CASE WHEN seat6_id IS NOT NULL THEN 1 ELSE 0 END) 
            + (CASE WHEN seat7_id IS NOT NULL THEN 1 ELSE 0 END) 
            + (CASE WHEN seat8_id IS NOT NULL THEN 1 ELSE 0 END) 
            + (CASE WHEN seat9_id IS NOT NULL THEN 1 ELSE 0 END) 
            + (CASE WHEN seat10_id IS NOT NULL THEN 1 ELSE 0 END)) AS sold_tickets FROM api_seats GROUP BY trip_id'''

            global seats
            with connection.cursor() as cursor:
             cursor.execute(sqlQ)
             seats = cursor.fetchall()

            filtrada = [] 
            for travel in seats:
                    trips = list(Trip.objects.filter(id=travel[1]).values())
                    filtrada.append({"id":travel[0],"avgSoldTickets":travel[2],
                                     "trip": trips[0]})

            datos = {'message': "trips avg", "trip": filtrada}
            return JsonResponse(datos)

    def post(self, request, capacity):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        try:
            numSoldTickets = math.floor(capacity/10)

            sqlQ =''' SELECT id, trip_id,
                ((CASE WHEN seat1_id IS NOT NULL THEN 1 ELSE 0 END) 
                + (CASE WHEN seat2_id IS NOT NULL THEN 1 ELSE 0 END) 
                + (CASE WHEN seat3_id IS NOT NULL THEN 1 ELSE 0 END) 
                + (CASE WHEN seat4_id IS NOT NULL THEN 1 ELSE 0 END) 
                + (CASE WHEN seat5_id IS NOT NULL THEN 1 ELSE 0 END) 
                + (CASE WHEN seat6_id IS NOT NULL THEN 1 ELSE 0 END) 
                + (CASE WHEN seat7_id IS NOT NULL THEN 1 ELSE 0 END) 
                + (CASE WHEN seat8_id IS NOT NULL THEN 1 ELSE 0 END) 
                + (CASE WHEN seat9_id IS NOT NULL THEN 1 ELSE 0 END) 
                + (CASE WHEN seat10_id IS NOT NULL THEN 1 ELSE 0 END)) AS sold_tickets, bus_id  
                FROM django_apiv1.api_seats'''

            global seats
            with connection.cursor() as cursor:
             cursor.execute(sqlQ)
             seats = cursor.fetchall()
  
            filtrada = []
            
            for travel in seats:
                
                if travel[2]>numSoldTickets:
                    filtrada.append({"id":travel[0],"trip_id":travel[1],
                                     "sold_tickets":travel[2],"bus_id":travel[3]})

            datos = {'message': "Success", "report":filtrada}
        except:
            datos = {'message': "Error generating report."}

        return JsonResponse(datos)
    
