# Generated by Django 5.1.7 on 2025-03-27 13:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0016_alter_submenu_contract'),
        ('ut', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationOrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Itemid', models.CharField(max_length=155)),
                ('Qty', models.IntegerField()),
                ('SalesId', models.CharField(max_length=155)),
                ('InventLocationId', models.CharField(max_length=155)),
                ('ConsigneeAccount', models.CharField(max_length=155)),
                ('DeliveryDate', models.DateField()),
                ('ManDate', models.DateField()),
                ('SalesUnit', models.CharField(default='шт', max_length=155)),
                ('Delivery', models.IntegerField(default=2)),
                ('Redelivery', models.IntegerField(default=1)),
                ('OrderType', models.IntegerField(default=1)),
                ('Comment', models.CharField(max_length=155)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationPorderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Itemid', models.CharField(max_length=155)),
                ('Qty', models.IntegerField()),
                ('PurchId', models.CharField(max_length=155)),
                ('InventLocationId', models.CharField(max_length=155)),
                ('VendAccount', models.CharField(max_length=155)),
                ('DeliveryDate', models.DateField()),
                ('PurchUnit', models.CharField(default='шт', max_length=155)),
                ('PurchTTN', models.IntegerField(default=1)),
                ('Price', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
            ],
        ),
        migrations.RemoveField(
            model_name='applicationporder',
            name='contract',
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ut.basemodel')),
                ('number', models.CharField(max_length=155)),
                ('date', models.DateField()),
                ('client', models.CharField(max_length=155)),
                ('stock', models.CharField(max_length=155)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_app.contracts')),
                ('filial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_app.filial')),
            ],
            bases=('ut.basemodel',),
        ),
        migrations.DeleteModel(
            name='ApplicationOrder',
        ),
        migrations.DeleteModel(
            name='ApplicationPorder',
        ),
        migrations.AddField(
            model_name='applicationporderitems',
            name='application',
            field=models.ManyToManyField(related_name='applications_porders', to='ut.application'),
        ),
        migrations.AddField(
            model_name='applicationorderitems',
            name='application',
            field=models.ManyToManyField(related_name='applications_orders', to='ut.application'),
        ),
    ]
