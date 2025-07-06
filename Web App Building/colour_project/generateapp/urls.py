from django.urls import path
from .views import random_color_view, random_color_view2, color_view, rgb_color_view, random_color_with_template_view,rgb_color_with_template

urlpatterns = [
    path('random', random_color_view),
    path('random2', random_color_view2),
    path('randomtemplate/', random_color_with_template_view),
    path('template/<int:red>/<int:green>/<int:blue>/', rgb_color_with_template),
    path('<str:color>', color_view),
    path('<int:red>/<int:green>/<int:blue>/', rgb_color_view),
    

]