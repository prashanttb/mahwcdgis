from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.homePage, name='homepage'),
    path('map', views.viewMap, name='map'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('what-we-do', views.about_wwd, name='what-we-do'),
    path('our-team', views.about_op, name='our-team'),
    path('partners', views.about_p, name='partners'),
    path('category', views.category, name='category'),
    path('category_1', views.category_1, name='category_1'),
    path('category_2', views.category_2, name='category_2'),
    path('category_3', views.category_3, name='category_3'),
    path('mr', views.homepage_mr, name='mr'),
    path('mr/contact_us', views.contact_us_mr, name='mr/contact_us'),
    path('mr/our-team', views.about_op_mr, name='mr/our-team'),
    path('mr/what-we-do', views.about_wwd_mr, name='mr/what-we-do'),
    path('mr/partners', views.about_p_mr, name='mr/partners'),
    
   
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

