# Generated by Django 3.1.7 on 2021-03-21 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MatchApp', '0042_auto_20210321_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='email',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='f_nacimiento',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento'),
        ),
        migrations.AddField(
            model_name='persona',
            name='nacionalidad',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='sexo',
            field=models.CharField(blank=True, choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='tel_cel',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Celular'),
        ),
        migrations.AddField(
            model_name='persona',
            name='tel_fijo',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='telefono fijo'),
        ),
    ]