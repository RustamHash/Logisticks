# Generated by Django 5.1.7 on 2025-03-28 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0016_alter_submenu_contract'),
    ]

    operations = [
        migrations.AddField(
            model_name='contracts',
            name='ftp_bool',
            field=models.BooleanField(default=False, verbose_name='Наличие ftp'),
        ),
    ]
