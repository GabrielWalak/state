from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.lista_nieruchomosci, name='lista_nieruchomosci'),
    path('nieruchomosci/dodaj/', views.dodaj_nieruchomosc, name='dodaj_nieruchomosc'),
    path('nieruchomosci/nieruchomosc_id/edytuj/', views.edytuj_nieruchomosc, name='edytuj_nieruchomosc'),
    path('najemcy/', views.lista_najemcow, name='lista_najemcow'),
    path('kalendarz/', views.kalendarz_najmow, name='kalendarz_najmow'),
    path('oplaty/', views.lista_oplat, name='lista_oplat'),
    path('raporty/', views.raporty, name='raporty'),
    path('ustawienia/', views.ustawienia, name='ustawienia'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)