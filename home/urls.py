from django.urls import path
from .views import HomeView
from . import views
app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('connect/<str:alpha>/<int:num>/', views.change_friends, name='change_friends'),
    path('message/<int:num>/', views.chat, name='chat'),
    path('mytweet/', views.tweets, name='tweets'),
    path('timeline/', views.publictweets, name='publictweets'),

]
