from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name="news"),
    path('prices/', views.prices, name="prices"),
    path('api/data/', views.get_data, name='api-data'),
    path('api/chart/data/', views.ChartData.as_view()),
    path('4chart/', views.fourcharts, name="fourcharts"),
]