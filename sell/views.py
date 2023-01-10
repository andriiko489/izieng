from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Link

def link(request, link_id):
    template = loader.get_template('sell/index.html')
    link=Link.objects.get(pk=link_id)
    context = {'link':link,'payment_link':'/payment/'+str(link.id)}
    return HttpResponse(template.render(context,request))
