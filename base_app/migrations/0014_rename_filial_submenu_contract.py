# Generated by Django 5.1.4 on 2025-03-26 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0013_submenu_filial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submenu',
            old_name='filial',
            new_name='contract',
        ),
    ]
