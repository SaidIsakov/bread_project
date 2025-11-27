from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
  class Meta:
    model = Contact
    fields = ['name', 'email', 'phon_number', 'message']
    widgets = {
      'name': forms.TextInput(attrs={
        'class': 'form-control'
      }),
      'phon_number': forms.TextInput(attrs={
        'class': 'form-control'
      }),
      'email': forms.TextInput(attrs={
        'class': 'form-control'
      }),
      'message': forms.Textarea(attrs={
        'class': 'form-control',
      })
    }
    labels = {
        'name': 'Имя',
        'phon_number': 'Телефон',
        'email': 'Email',
        'message': 'Сообщение'
    }
