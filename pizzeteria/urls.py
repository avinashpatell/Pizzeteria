"""Define URLs Pattern for Pizzeteria."""

from django.urls import re_path
from . import views

app_name="Pizza"

urlpatterns=[
    #Home Page
    re_path('^$',views.index,name='index'),
    re_path(r'^pizza/$', views.pizza, name='pizza'),
    re_path(r'^pizza/(?P<pizza_id>\d+)/$', views.toppings, name='pizza'),
]