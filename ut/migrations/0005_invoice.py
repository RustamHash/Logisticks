# Generated by Django 5.1.7 on 2025-04-01 13:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ut', '0004_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('program_id', models.IntegerField(verbose_name='')),
                ('acs_number', models.CharField(max_length=155, verbose_name='')),
                ('is_active', models.BooleanField(verbose_name='')),
                ('date_doc', models.DateField(verbose_name='')),
                ('is_entry', models.BooleanField(verbose_name='')),
                ('invoice_type_id', models.IntegerField(verbose_name='')),
                ('from_req_id', models.IntegerField(verbose_name='')),
                ('to_req_id', models.IntegerField(verbose_name='')),
                ('date_create', models.DateField(verbose_name='')),
                ('date_update', models.DateField(blank=True, null=True, verbose_name='')),
                ('comment', models.CharField(blank=True, max_length=155, null=True, verbose_name='')),
                ('user_create', models.CharField(max_length=155, verbose_name='')),
                ('user_update', models.CharField(blank=True, max_length=155, null=True, verbose_name='')),
                ('delivery', models.BooleanField(verbose_name='')),
                ('uid', models.IntegerField(verbose_name='')),
                ('order_number', models.CharField(blank=True, max_length=155, null=True)),
                ('agent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice', to='ut.agent', verbose_name='')),
                ('from_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice_from', to='ut.agent', verbose_name='')),
                ('to_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice_to', to='ut.agent', verbose_name='')),
            ],
        ),
    ]
