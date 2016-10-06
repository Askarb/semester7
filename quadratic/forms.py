from django import forms


class QuadraticForm(forms.Form):
    a = forms.FloatField(widget=forms.TextInput(attrs={'class': 'number'}), label='a', max_value=100000, min_value=-100000)
    b = forms.FloatField(widget=forms.TextInput(attrs={'class': 'number'}), label='b', max_value=100000, min_value=-100000)
    c = forms.FloatField(widget=forms.TextInput(attrs={'class': 'number'}), label='c', max_value=100000, min_value=-100000)


