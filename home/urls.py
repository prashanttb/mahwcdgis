from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.homePage, name='homepage'),
   
    #path('aboutus', views.aboutUs, name='aboutus'),
    path('map', views.viewMap, name='map'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('what-we-do', views.about_wwd, name='what-we-do'),
    path('our-team', views.about_op, name='our-team'),
    path('partners', views.about_p, name='partners'),
    path('category', views.category, name='category'),
    path('category_1', views.category_1, name='category_1'),
    path('category_2', views.category_2, name='category_2'),
    path('category_3', views.category_3, name='category_3')
    
   
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

