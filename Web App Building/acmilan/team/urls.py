from django.urls import path
from .views import *

urlpatterns = [
    path('dreamteam', dreamteam_view),
    path('dreamteam_hardcodat/', dreamteam_hardcodat_view),
    path('listajucatori', lista_jucatori_view),
]