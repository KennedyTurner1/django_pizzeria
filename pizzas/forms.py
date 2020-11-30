from django import forms

from .models import Pizza

class PizzaForm(forms.ModelForm):
    class Meta: #a meta class defines the behavior of PizzaForm
        model = Pizza
        fields = ['name']
        labels = {'name': ''}
        widgets = {'name': forms.Textarea(attrs={'cols':80})}