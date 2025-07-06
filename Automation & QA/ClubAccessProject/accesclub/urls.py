from django.urls import path
from .views import validare_cnp_view

urlpatterns = [ 

    path('', validare_cnp_view)
]