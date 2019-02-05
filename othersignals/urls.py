from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.signalshome, name='Signals'),
    path('bitcoinity/', views.bitcoinity, name='bitcoinity_app'),
    path('coinfarm/', views.coinfarm, name='coinfarm'),
    path('datamish/', views.datamish, name='datamish'),
    path('cryptowatch/', views.cryptowatch, name='cryptowatch'),
    path('tokenmonitor/', views.tokenmonitor, name='tokenmonitor'),
    path('tucsky/', views.tucsky, name='tucsky'),
    path('rsialerts/', views.rsialerts, name='rsialerts'),
    path('alternative/', views.alternative, name='alternative'),
]