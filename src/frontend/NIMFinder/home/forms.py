from django import forms

class ActionForm(forms.Form):
    ACTION = forms.CharField(label='', max_length=100,)