

from django.urls import path
from .views import *


urlpatterns = [
    path('', chess_table_view),
    path('<int:N>', chess_table_view),
    path('<int:N>/<int:sol_no>', chess_table_view, name='chess_table_url_with_sol_no'),
    path('json/<int:N>', json_chess_table_view),

    path('spa/<int:N>', spa_chess_table_view),
    path('spa/json/<int:N>', json_spa_chess_table_view)
]