from django.db import models
from django.core.validators  import MaxValueValidator, MinValueValidator
#   min and max  تحديدي  ال 
# Create your models here.
# >>>>   python manage.py sqlmigrate pationt 0001
# >>>>   python manage.py shell  
#  shell :  تطبيق داخلي يخليك  تتعامل مع البيانات  بشكل مباشر 
     
class Patient(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField( max_length=100)
    age = models.IntegerField( validators=[MinValueValidator(1) , MaxValueValidator(100)])
    heartrate = models.IntegerField(validators=[MaxValueValidator(120) , MinValueValidator(2)] , default=1)
    def __str__(self):
        return f"{self.fname} - {self.lname} and my age {self.age}" 




