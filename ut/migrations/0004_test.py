# Generated by Django 5.1.7 on 2025-04-01 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ut', '0003_agent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=155)),
            ],
        ),
    ]
