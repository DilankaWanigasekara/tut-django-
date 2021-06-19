from django.shortcuts import render
from django.http import JsonResponse

def addnumber(request,num1,num2):
    sum= {
        "total": num1 + num2
    }
    return JsonResponse(sum)

def reducenumber(request,num1,num2):
    sum= {
        "sum": num1 - num2
    }
    return JsonResponse(sum)
def multiplynumber(request,num1,num2):
    sum= {
        "sum": num1 * num2
    }
    return JsonResponse(sum)

def devidenumber(request,num1,num2):
    if (num2) == 0 :
        message={
        'message' : 'devide by zero exception'
        }
    return JsonResponse(message)
    sum = {
        "sum": num1 / num2
    }
    return JsonResponse(sum)
