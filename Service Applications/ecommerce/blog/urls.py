from django.urls import path
from .views import *

urlpatterns = [
    path('', blog_list_view, name='home_blog'),
    path('<slug>', blog_details_view)
]