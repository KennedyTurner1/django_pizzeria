from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta: #a meta class defines the behavior of PizzaForm
        model = Comment
        fields = ['text']
        widgets = {'text':forms.Textarea(attrs={'cols':80})}