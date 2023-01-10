from django.forms import ModelForm

from sell.models import Card

class PaymentForm(ModelForm):
    class Meta:
        model = Card
        exclude = ('id','link_id')
