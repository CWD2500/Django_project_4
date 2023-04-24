from django.shortcuts import render
from .models import Patient
from  . import models

# Create your views here.


def patientList(request):
    patient = models.Patient.objects.all()
    context = {
        'patient':patient
    }
    return render(request , 'patient/index.html' , context)