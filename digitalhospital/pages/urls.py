
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("fizyoloji",views.fizyoloji),
    path("hastaliklar",views.hastaliklar ,name="hastaliklar"),
    path("iletisim",views.iletisim,name="iletisim"),
    path("doktorlar",views.doktorlar),
    path("egitimler",views.egitimler),


     path('hastaliklar/<slug:slug>/',views.hastalik_detay, name='hastalik_detay'),
     
     path('gorus-gonder/',views.gorus_gonder, name='gorus_gonder'),

    path("tahmin/", views.predict_view, name="tahmin"),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)