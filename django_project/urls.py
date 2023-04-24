"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from django.urls import path , include
from . import views

urlpatterns = [
    # path('' , views.homPage ),
    path('admin/', admin.site.urls),
    # path('my_app/' , include('my_app.urls')),
    # path('student/' , include('student.urls')),
    # path('patient/' , include('pationt.urls')),
    # path('home/' , include('classViews.urls')),
    # path('ViewForm/' , include('ViewForm.urls') ),
    path('Employee/'  , include('ClasaViewForm.urls')),
    path('store/'  , include('WebSite.urls')),
    path('storePost/'  , include('WebSitePosts.urls')),
    path(''  , include('AuthUser.urls')),
      
]
# settings.DEBUG   لانو نحنا بدنا نجيب صور  فا لازن نكتب بي البيئة التطويرية  هاد 
# settings.DEBUG  :   لازم نحط  True  اذا كنا 
# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
