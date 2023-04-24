from django.db import models
from django.contrib.auth.models import  User
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    post_type = models.CharField(max_length=255)
    description = models.TextField(null=True , blank=True)
    image =  models.ImageField( upload_to='image', default="images/no-image.jpg"  , blank=True , null=True)
    created_add =  models.DateTimeField( auto_now=True, auto_now_add=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE , null=True , blank=True)    
    


    def __str__(self):
        return self.title
    
    # class  Meta :    هو كلاس  يعطي معملومات اضافية 
    class Meta:
        # post جيب  المعلوماى  اخر وحد  يعني اعمل اول واحد اهر شي   يعني اخر 
        ordering = ['created_add']


