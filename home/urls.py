from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.homePage, name='homepage'),
   
    path('aboutus', views.aboutUs, name='aboutus'),
    path('map', views.viewMap, name='map'),
    path('contact', views.viewMap, name='contact'),
   
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

