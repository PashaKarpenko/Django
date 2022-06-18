from django.urls import path
from .views import hellodjango, helloname, todaydate, year, month, day

urlpatterns = [
    path('', hellodjango),
    path('date/', todaydate),
    path('date/year/', year),
    path('date/month/', month),
    path('date/day/', day),
    path('<str:name>/', helloname)
]