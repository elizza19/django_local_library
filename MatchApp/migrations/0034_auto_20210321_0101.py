# Generated by Django 3.1.7 on 2021-03-21 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MatchApp', '0033_auto_20210321_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='tel_cel',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='tel_fijo',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='telefono fijo'),
        ),
    ]
