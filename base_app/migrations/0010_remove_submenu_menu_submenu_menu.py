# Generated by Django 5.1.4 on 2025-03-26 22:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0009_remove_submenu_menu_submenu_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submenu',
            name='menu',
        ),
        migrations.AddField(
            model_name='submenu',
            name='menu',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='base_app.menu', verbose_name='Меню'),
            preserve_default=False,
        ),
    ]
