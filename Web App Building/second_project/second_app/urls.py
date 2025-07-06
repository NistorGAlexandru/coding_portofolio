from django.urls import path
from .views import view_exemplu, nume_intreg, view_404, view_dublu, view_adunare, view_concatenare

urlpatterns = [
    path('example/', view_exemplu),
    path('fullname/', nume_intreg),
    path('404/', view_404),
    path('power/<int:x>/', view_dublu),
    path('sum/<int:x>/<int:y>/', view_adunare),
    path('concatenation/', view_concatenare)

]