from django.urls import path
from django.conf.urls import url

from .views import render
from . import views

app_name = 'Potluck'



urlpatterns = [
    path('', views.potluck, name='Home'),
    path('Bear/', views.bearmarkets, name='Bear News'),
    path('Bull/', views.bullmarkets, name='Bull News'),
    path('New/', views.newpotlucknews, name='New News'),
    path('Top/', views.toppotlucknews, name='Top News'),
    path('Shit/', views.shitcoinNnews, name='Shit News'),
    path('NewPost/', views.userpost, name='NewPost'),
    path('BotGarage/', views.bottweak, name='BotTweaking'),
    path('PoliticalNews/', views.politics, name='PoliticalNews'),
    url('(?P<pk>[0-9]+)/upvote', views.upvote, name='upvote'),
    url('(?P<pk>[0-9]+)/downvote', views.downvote, name='downvote'),

]

# <app> /<model>_<viewtype>.html