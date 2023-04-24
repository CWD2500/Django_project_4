from django.urls import path
from .views  import  Home , Create , Delete , Details , Update





urlpatterns = [
    path('' , Home.as_view()  , name="home" ),
    path('create/' , Create.as_view()  , name="create" ),
    path('update/<int:pk>/' , Update.as_view()  , name="update" ),
    path('detail/<int:pk>/' , Details.as_view()  , name="detail" ),
    path('delete/<int:pk>/' , Delete.as_view()  , name="Delete" ),

]
