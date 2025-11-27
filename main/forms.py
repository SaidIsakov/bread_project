from django import forms
from .models import Contact
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):
  class Meta:
    model = Contact
    fields = ['name', 'email', 'phon_number', 'message']
    labels = {
        'name': 'Имя',
        'phon_number': 'Телефон',
        'email': 'Email',
        'message': 'Сообщение'
    }

  def __init__(self, *args, **kwargs):
      super(ContactForm, self).__init__(*args, **kwargs)

      for name, field in self.fields.items():
          field.widget.attrs.update({'class': 'form-control'})



