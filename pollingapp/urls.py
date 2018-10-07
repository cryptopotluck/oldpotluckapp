from django.urls import path

from . import views

app_name = "pollingapp"
urlpatterns = [
    path('vote/', views.index, name="vote"),

]