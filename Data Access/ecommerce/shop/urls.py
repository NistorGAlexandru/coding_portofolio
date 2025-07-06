
## URL - din aplicatia shop
from django.urls import path
from .views import *

urlpatterns = [
    path('products/', product_list_view, name='all_products_url'),
    path('products/<slug>', product_details),
    path('sesiune/', sesiune_view),
    path('cookie/', cookie_view),
] 