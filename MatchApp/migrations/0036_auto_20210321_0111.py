# Generated by Django 3.1.7 on 2021-03-21 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MatchApp', '0035_auto_20210321_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='dni',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='sexo',
            field=models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=20, null=True),
        ),
    ]
