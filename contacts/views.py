# Create your views here.
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic import (
        View, 
        ListView,
        CreateView,
        UpdateView,
        DeleteView,
        DetailView)

from contacts.models import Contact

def hello_word(request):
    return HttpResponse("Hello, World")

class MyView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World")

class ListContactView(ListView):
    model = Contact
    template_name = 'contacts_list.html'


class CreateContactView(CreateView):
    model = Contact
    template_name = 'edit_contact.html'

    def get_success_url(self):
        return reverse('contacts-list')

    def get_context_data(self, **kwargs):
        context = super(CreateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts-new')
        return context

class UpdateContactView(UpdateView):
    model = Contact 
    template_name = 'edit_contact.html'

    def get_success_url(self):
        return reverse('contacts-list')

    def get_context_data(self, **kwargs):
        context = super(UpdateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts-edit',
                kwargs={'pk': self.get_object().id})
        return context

class DeleteContactView(DeleteView):
    model = Contact
    template_name = 'delete_contact.html'

    def get_sucess_url(self):
        return reverse('contacts-list')

class ContactView(DetailView):
    model = Contact
    template_name = 'contact.html'

