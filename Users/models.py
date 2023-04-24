from django.db import models
from django.contrib.auth.models import User
from PIL  import Image
# Create your models here.


class ProFile(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)


    avater  = models.ImageField( upload_to='prFile')

    def __str__(self):
        return f"{self.user.username} ProFile"
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) # Call the real save() method

        image = Image.open(self.avater.path)
        if image.height>400 or image.width>500:
            output_size = (300, 300)  #     400 اذا كان اكب من 
            #   ف من صغرها 
            image.thumbnail(output_size)
            image.save(self.avater.path)