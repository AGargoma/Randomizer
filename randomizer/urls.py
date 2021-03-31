from django.urls import path

from randomizer import views

urlpatterns = [
    path('',views.randomize, name='randomizer'),
]