from os import name
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import Settings, settings
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View, TemplateView, CreateView
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()

# Formas de chamar minha view

#class IndexView(object):
#    def __call__(self, request):
#        return render(request, 'index.html')
#index = IndexView()
#-------------------------------------------

#class IndexView(View):
#    def get (self, request):
#        return render(request, 'index.html')
#index = IndexView.as_view()

class IndexView(TemplateView):
    template_name = 'index.html'
index = IndexView.as_view()

def contact(request):
    success = False  
    form = ContactForm(request.POST or None)   
    if form.is_valid():
        form.send_mail()
        success = True 
    elif request.method == 'POST':
        messages.error(request, 'Formulário inválido')
    context = {
        'form': form,
        'success': success
    }
    return render (request, 'contact.html', context)

    



