from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.homePage, name='homepage'),
   
    #path('aboutus', views.aboutUs, name='aboutus'),
    path('map', views.viewMap, name='map'),
    path('contact', views.viewMap, name='contact'),
    path('what-we-do', views.about_wwd, name='what-we-do'),
    path('our-team', views.about_op, name='our-team'),
    path('partners', views.about_p, name='partners'),
    path('category', views.category, name='category')
   
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

