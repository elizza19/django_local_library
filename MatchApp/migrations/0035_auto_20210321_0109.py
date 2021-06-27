# Generated by Django 3.1.7 on 2021-03-21 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MatchApp', '0034_auto_20210321_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='tipo_fam',
            field=models.CharField(blank=True, choices=[('Familia', 'Familia'), ('Adulto(s)', 'Adulto(s)'), ('Joven <25', 'Joven <25'), ('Senior', 'Senior')], max_length=20, null=True, verbose_name='Tipo de Familia'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='tipo_viv',
            field=models.CharField(blank=True, choices=[('Casa', 'Casa'), ('Depa', 'Depa')], max_length=20, null=True, verbose_name='Tipo de Vivienda'),
        ),
    ]
