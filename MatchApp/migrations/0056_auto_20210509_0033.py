# Generated by Django 3.1.7 on 2021-05-08 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MatchApp', '0055_auto_20210509_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrevista',
            name='puntuacion',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, verbose_name='Puntuacion'),
        ),
    ]