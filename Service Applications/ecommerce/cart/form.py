from django import forms


value_choices = ((1,'1'), (2,'2'), (3,'3'))
value_choices = ((i, str(i) + "buc" ) for i in range(1, 21))


class AddToCartForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=value_choices)


