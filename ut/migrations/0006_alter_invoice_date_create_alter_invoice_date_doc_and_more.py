# Generated by Django 5.1.7 on 2025-04-01 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ut', '0005_invoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='date_create',
            field=models.DateTimeField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_doc',
            field=models.DateTimeField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_update',
            field=models.DateTimeField(blank=True, null=True, verbose_name=''),
        ),
    ]
