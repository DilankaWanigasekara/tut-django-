from django.shortcuts import render
from django.http import JsonResponse

def getVehicle(request):
    vehicle={
        'id':1,
        'type':'car',
        'color':'black'
        }

    return JsonResponse(vehicle) #return vehicle as json response 
def getPerson(request):

    person = {
        'name': 'chithara',
        'age': 60
    }

    return JsonResponse(person)

def getVehiclebyId(request, id):
    vehicles = [
        {
            'id': 1,
            'type': 'car',
            'color': 'black'
        },
        {
            'id': 4,
            'type': 'van',
            'color': 'black'
        },
        {
            'id': 7,
            'type': 'bike',
            'color': 'black'
        },
        {
            'id': 3,
            'type': 'boat',
            'color': 'black'
        }
    ]

    
    for v in vehicles:               # loop through the json array one by one
        json_str = json.dumps(v)     # converts the json to a json string
        resp = json.loads(json_str)  # loads the json string
        if resp['id'] == id:         # checks for matching vehicle id
            return JsonResponse(v)   # returns matched vehicle object with the requested id

    # this part will be executed if an vehicle was not found
    message = {
        'message': 'vehicle of id ' + str(id) + ' cannot be found'
    }

    
    return JsonResponse(message)     # it will rerurn the above "not found" message as the response


def addNumbers(request, num1, num2):
    sum = {
        "total": num1 + num2
    }
    return JsonResponse(sum)