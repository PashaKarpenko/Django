from django.http import HttpResponse, HttpRequest
import datetime


def hellodjango(request: HttpRequest):
    return HttpResponse('Hello Django!')

def todaydate(request: HttpRequest):
    today = datetime.date.today()
    date_conv = today.strftime('%d.%m.%Y')
    return HttpResponse(date_conv)

def year(request: HttpRequest):
    today = datetime.date.today()
    year = today.strftime('%Y')
    return HttpResponse(year)

def month(request: HttpRequest):
    today = datetime.date.today()
    month = today.strftime('%m')
    return HttpResponse(month)

def day(request: HttpRequest):
    today = datetime.date.today()
    day = today.strftime('%d')
    return HttpResponse(day)



def helloname(request: HttpRequest, name):
    return HttpResponse(f"Hello {name}!")
