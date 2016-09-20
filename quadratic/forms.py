from django import forms


class quadratic_form(forms.Form):
    a = forms.FloatField(widget=forms.TextInput(attrs={'class': 'number'}), label='a', max_value=1000, min_value=-1000)
    b = forms.FloatField(widget=forms.TextInput(attrs={'class': 'number'}), label='b', max_value=1000, min_value=-1000)
    c = forms.FloatField(widget=forms.TextInput(attrs={'class': 'number'}), label='c', max_value=1000, min_value=-1000)

