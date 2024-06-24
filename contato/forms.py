from django import forms
from contato.models import Contact
import re




class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    
    def clean_cell_number(self):
        number = self.cleaned_data.get('cell_number')
        
        pattern = re.compile(r'^\(\d{3}\)\d{5}-\d{4}$')

        if not pattern.match(number):
            raise forms.ValidationError('O número de telefone deve estar no formato (ddd)xxxxx-xxxx.')
        
        return number
