# Generated by Django 3.1.7 on 2021-03-21 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MatchApp', '0032_auto_20210321_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='tel_cel',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='tel_fijo',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='telefono fijo'),
        ),
    ]
