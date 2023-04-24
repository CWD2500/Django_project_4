from django.urls import path
from .import views

urlpatterns = [
    path('' , views.patientList , name ='patientList')
]
