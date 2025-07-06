from django.urls import path, include
from .views import access_view, rezultat_view, django_form_view

urlpatterns = [
    path('acces/', access_view),
    path('rezultat', rezultat_view, name = "rezultat"),
    path('djangoform/', django_form_view)
]