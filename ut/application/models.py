from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save, pre_init

from base_app.models import Filial, Contracts
from django.dispatch import receiver


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Application(BaseModel):
    # id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=155)
    date = models.DateField()
    client = models.CharField(max_length=155)
    stock = models.CharField(max_length=155)
    contract = models.ForeignKey(Contracts, on_delete=models.CASCADE)
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE)


class ApplicationOrderItems(models.Model):
    Itemid = models.CharField(max_length=155)
    Qty = models.IntegerField()
    SalesId = models.CharField(max_length=155)
    InventLocationId = models.CharField(max_length=155)
    ConsigneeAccount = models.CharField(max_length=155)
    DeliveryDate = models.DateField()
    ManDate = models.DateField()
    SalesUnit = models.CharField(max_length=155, default='шт')
    Delivery = models.IntegerField(default=2)
    Redelivery = models.IntegerField(default=1)
    OrderType = models.IntegerField(default=1)
    Comment = models.CharField(max_length=155)
    application = models.ManyToManyField(Application, related_name='applications_orders')


class ApplicationPorderItems(models.Model):
    Itemid = models.CharField(max_length=155)
    Qty = models.IntegerField()
    PurchId = models.CharField(max_length=155)
    InventLocationId = models.CharField(max_length=155)
    VendAccount = models.CharField(max_length=155)
    DeliveryDate = models.DateField()
    PurchUnit = models.CharField(max_length=155, default='шт')
    PurchTTN = models.IntegerField(default=1)
    Price = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    application = models.ManyToManyField(Application, related_name='applications_porders')

# @receiver(pre_init, sender=Application)
# def fill_place(sender, instance, **kwargs):
#     instance.filial = instance.contract.filial
