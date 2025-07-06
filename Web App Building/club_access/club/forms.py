from django import forms


class AccessForm(forms.Form):
    # birthday = forms.DateField(label = 'Selecteaza o data')
    varsta = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'varsta'}))
    choices = [('m', 'Masculin'),
                ('f', 'Feminin')]
    
    gen = forms.ChoiceField(choices = choices, required = True, widget = forms.Select)
    sex = forms.ChoiceField(choices = choices, required = True, widget = forms.RadioSelect)