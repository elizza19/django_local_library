# Generated by Django 3.1.7 on 2021-05-11 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MatchApp', '0062_auto_20210511_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apadrinamiento',
            name='monto_pactado',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Monto Pactado (S/.)'),
        ),
        migrations.AlterField(
            model_name='apadrinamiento',
            name='pag_prom_men',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Pago prom mensual (S/.)'),
        ),
    ]