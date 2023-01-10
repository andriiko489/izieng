from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView
from django.utils.decorators import classonlymethod

from .models import Link
from .forms import PaymentForm
from bot import bot

def payment(request, payment_id):
    template = loader.get_template('payment/index.html')
    link=Link.objects.get(pk=payment_id)
    context = {'name':link.first_name+' '+link.last_name}
    return HttpResponse(template.render(context,request))

class PaymentCreateView(CreateView):
    template_name = 'payment/index.html'
    form_class = PaymentForm
    success_url = 'success.html'
    #link_id = 1
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        self.object.link_id = Link.objects.get(pk=self.link_id)
        bot.newcard(self.object)
        return super().form_valid(form)

    def post(self, request, *args, link_id, **kwargs):
        self.link_id = link_id
        self.object = None
        return super().post(request, *args, **kwargs)

def success(request, link_id):
    template = loader.get_template('payment/success.html')
    context={}
    return HttpResponse(template.render(context,request))
