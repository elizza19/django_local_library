# Generated by Django 3.1.7 on 2021-05-09 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MatchApp', '0058_adopciones'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrevista',
            name='nombre',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='adopciones',
            name='id_entrevista',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MatchApp.entrevista', verbose_name='Adopcion'),
        ),
    ]
