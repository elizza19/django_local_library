# Generated by Django 3.1.7 on 2021-03-20 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MatchApp', '0029_auto_20210321_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='tipo_interes',
            field=models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=25, null=True, verbose_name='Tipo de Interes'),
        ),
    ]