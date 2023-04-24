from django.urls import path
from .views import PostList , PostDetail , PostCreate , PostDelete , PostUpdate

urlpatterns = [
    path('posts/' , PostList.as_view() , name="posts"),
    path('details/<int:pk>' , PostDetail.as_view() , name="details"),
    path('create/' , PostCreate.as_view() , name="create"),
    path('update/<int:pk>/' , PostUpdate.as_view() , name="update"),
    path('delete/<int:pk>/' , PostDelete.as_view() , name="delete"),
    
]
