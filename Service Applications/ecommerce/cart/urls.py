from django.urls import path
from .views import *


urlpatterns = [ 
    path('add/<product>/', add_to_cart_view, name='add_to_cart_url'),
    path('', cart_view, name='cart_view_url'),
    path('clear', clear_cart,
         name='clear_cart_url'),
    path('remove/<product>', remove_product_view, name='remove_product_url')
    
]