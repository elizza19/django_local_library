# Generated by Django 3.1.7 on 2021-05-11 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MatchApp', '0061_apadrinamiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apadrinamiento',
            name='tipo_ingreso',
            field=models.CharField(blank=True, choices=[('Combinado', 'Combinado'), ('Unico', 'Unico'), ('Directo Albergue', 'Directo Albergue')], max_length=20, null=True, verbose_name='Tipo de Ingreso'),
        ),
    ]