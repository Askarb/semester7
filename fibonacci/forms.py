from django import forms


class FibonacciForm(forms.Form):
    a = forms.IntegerField(max_value=1000000000, min_value=1)
    #a = forms.FloatField(widget=forms.TextInput(attrs={'class': 'number'}), label='a', max_value=100000, min_value=-100000)


