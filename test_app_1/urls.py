from django.urls import path

from .views import foo, first

urlpatterns = [
    path('foo/', foo),
    path('first/', first)
]