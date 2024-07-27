from contato.models import Contact
from django.urls import reverse_lazy
from contato.forms import ContactForm
from django.views.generic import CreateView


class NewContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'new_contact.html'
    success_url = reverse_lazy('home')
