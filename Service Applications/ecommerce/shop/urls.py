
## URL - din aplicatia shop
from django.urls import path
from .views import *

urlpatterns = [
    path('products/', product_list_view, name='all_products_url'),
    path('products/<slug>', product_details,
         name='product_details_url'),
    path('category/<slug>', category_details_view, name='category_details_url'),
    path('sesiune/', sesiune_view),
    path('cookie/', cookie_view),
    path('api/products/', ProductListView.as_view()),
    path('api/products/new', CreateNewProductView.as_view())
] 