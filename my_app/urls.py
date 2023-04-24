from django.urls import path
from . import views

#  urlpatterns  : list Path
urlpatterns = [
    path('' , views.index  , name="index"),
    path('about/' , views.my_about  , name="my_about"),
    path('teachre/' , views.index  , name="my_teachre"),
    path('<int:number1>/<int:number2>' , views.my_result  , name="my_result"),
    path('<str:fName>/<str:lName>' , views.my_name  , name="my_name"),
     

]




