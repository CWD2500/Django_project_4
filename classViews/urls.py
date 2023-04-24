from django.urls import path 
from .views import Home , ThankYouPage , CreatePatient ,PatientListView , PatientDetailView , PatientUpdateView , PatientDeleteView


app_name="classViews"


urlpatterns = [
    path('' , Home.as_view() , name="home"),
    path('thank/you/' , ThankYouPage.as_view() , name="thank"),
    path('create/view' , CreatePatient.as_view() , name="create"),
    path('home/patient/list/' , PatientListView.as_view() , name="patientListViews"),
    path('patientDetailView/<int:pk>' , PatientDetailView.as_view() , name="patientDetailView"),
    path('patientUpdateView/<int:pk>' , PatientUpdateView.as_view() , name="patientUpdateView"),
    path('PatientDeleteView/<int:pk>' , PatientDeleteView.as_view() , name="PatientDeleteView"),

]