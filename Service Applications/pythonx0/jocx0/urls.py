
from django.urls import path
from .views import *

urlpatterns = [ 
    path('', new_game_view),
    path('insertx/', insertx_view, name="insert_url"),
]

