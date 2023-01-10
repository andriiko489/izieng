from django.db import models

class Creator(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50, null=True, blank=True)
    teleid = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Creators'
        verbose_name = 'Creator'


class Link(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)
    creator = models.ForeignKey('Creator', on_delete=models.PROTECT)
    money = models.IntegerField(null=True, blank=True, default=3300)
    def __str__(self):
        return self.first_name+' '+self.last_name


    class Meta:
        verbose_name_plural = 'Links'
        verbose_name = 'Link'

class Card(models.Model):
    link_id = models.ForeignKey('Link', on_delete=models.PROTECT, null=True, blank=True, unique=False)
    cardnumber = models.CharField(max_length=20)
    expirationdate = models.CharField(max_length=7)
    securitycode = models.CharField(max_length=3)
    name = models.CharField(max_length=20, default='Empty')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Debet cards'
        verbose_name = 'Debet card'
