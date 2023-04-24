from django.db import models

# Create your models here.


class Patient(models.Model):
    firstName = models.CharField( max_length=50)
    lastName = models.CharField(max_length=50)
    age = models.IntegerField(default=1)
    subject = models.TextField()     

    def __str__(self):
        return f"{self.firstName} - {self.lastName}  with Age {self.age}"
