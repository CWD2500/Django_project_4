from django.db import models

# Create your models here.


class EmP(models.Model):
    name = models.CharField(max_length=50)
    age  = models.IntegerField(default=10)
    level = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    