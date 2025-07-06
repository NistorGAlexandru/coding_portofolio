from django.urls import path
from .views import home_view, contact_view, last_year_view, about_us_view

urlpatterns = [
    path('', home_view, name='home'),
    path('despre_noi/', about_us_view, name='about_us'),
    path('editia_trecuta/', last_year_view, name='last_year'),
    path('contact/', contact_view, name='contact'),

]