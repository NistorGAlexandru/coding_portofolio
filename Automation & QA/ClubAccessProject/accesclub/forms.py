from cnp import este_valid, are_acces
from django import forms
from django.core.exceptions import ValidationError

def form_validator(cnp):
    if not este_valid(cnp):
        raise ValidationError("CNP-ul introdus nu este valid")
    
def form_access_validator(cnp):
    if not are_acces(cnp):
        raise ValidationError("Nu aveti varsta necesara accesului")



class CNPForm(forms.Form):
    cnp = forms.CharField(max_length=13, validators=[ form_access_validator])