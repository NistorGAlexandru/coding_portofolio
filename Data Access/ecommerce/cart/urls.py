from django.urls import path
from .views import *


urlpatterns = [ 
    path('add/<product>/', add_to_cart_view, name='add_to_cart_url'),
    path('', cart_view, name='cart_view_url')
]