from django.urls import path
from .views  import Home  , Create   , Update , Details , Delete
urlpatterns = [
     
     path('' , Home.as_view() , name="home" ),
     path('create/' , Create.as_view() , name="created" ),
     path('update/<int:pk>/' , Update.as_view()  , name="Update"),
     path('details/<int:pk>/' , Details.as_view()  , name="detail"),
     path('Delete/<int:pk>/' , Delete.as_view()  , name="Delete"),

]
 