from django.urls import path
from . import views

app_name = 'student'
# Name Applcation 


urlpatterns = [
    path('' , views.allStudent  , name="allStudent"),
    path('add/student/' , views.addStudent , name="addStudent"),
    path('edit/student/' , views.editStudent , name="editStudent"),
    
]
