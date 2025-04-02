# Generated by Django 5.1.7 on 2025-04-01 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ut', '0011_alter_agent_agent_dovoz_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='agent',
            name='agent_dovoz_id',
            field=models.IntegerField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='agent',
            name='agent_id',
            field=models.IntegerField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='agent',
            name='comment',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='agent',
            name='contact_face',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='agent',
            name='contact_phone',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='agent',
            name='date_create',
            field=models.DateTimeField(blank=True, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='agent',
            name='date_update',
            field=models.DateTimeField(blank=True, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='agent',
            name='ex_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='agent',
            name='group_id',
            field=models.IntegerField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='agent',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='ИД'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='is_active',
            field=models.BooleanField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='agent',
            name='item_name',
            field=models.CharField(max_length=255, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='agent',
            name='level_id',
            field=models.IntegerField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='agent',
            name='program_id',
            field=models.IntegerField(verbose_name='ИД Программы'),
        ),
    ]
