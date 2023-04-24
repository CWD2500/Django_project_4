from django.urls  import path
from .views  import HomeView , ProFileView , LoginView,LogoutView , RegisterView
urlpatterns = [
    path('home/' , HomeView.as_view() , name="home" ),
    path('proFile/' , ProFileView.as_view() , name="proFile" ),
    path('login/' , LoginView.as_view() , name="login" ),
    path('logout/' , LogoutView.as_view(next_page='login') , name="logout" ),
    path('register/' , RegisterView.as_view() , name="register" ),
]
