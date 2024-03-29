# Generated by Django 3.1.7 on 2021-03-18 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MatchApp', '0022_auto_20210316_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascotas',
            name='alergias',
            field=models.CharField(blank=True, choices=[('Si', 'Si'), ('No', 'No')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='mascotas',
            name='descripcion',
            field=models.CharField(blank=True, max_length=9000, null=True, verbose_name='Descripcion en Web'),
        ),
        migrations.AddField(
            model_name='mascotas',
            name='enfermedad_cronica',
            field=models.CharField(blank=True, choices=[('Si', 'Si'), ('No', 'No')], max_length=20, null=True, verbose_name='enfermedad cronica'),
        ),
        migrations.AddField(
            model_name='mascotas',
            name='esterilizado',
            field=models.CharField(blank=True, choices=[('Si', 'Si'), ('No', 'No')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='mascotas',
            name='historia',
            field=models.CharField(blank=True, max_length=9000, null=True, verbose_name='Historia'),
        ),
        migrations.AddField(
            model_name='mascotas',
            name='id_color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MatchApp.color', verbose_name='color'),
        ),
        migrations.AddField(
            model_name='mascotas',
            name='peso_adulto',
            field=models.IntegerField(blank=True, null=True, verbose_name='Peso de Adulto'),
        ),
        migrations.AddField(
            model_name='mascotas',
            name='sexo',
            field=models.CharField(blank=True, choices=[('Macho', 'Macho'), ('Hembra', 'Hembra')], max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='mascotas',
            name='tamano_adulto',
            field=models.CharField(blank=True, choices=[('Pequeno', 'Pequeno'), ('Mediano', 'Mediano')], max_length=10, null=True, verbose_name='Tamano de Adulto'),
        ),
        migrations.AddField(
            model_name='mascotas',
            name='tipo_pelo',
            field=models.CharField(blank=True, choices=[('Largo', 'Largo'), ('Mediano', 'Mediano'), ('Corto', 'Corto'), ('Sin Pelo', 'Sin Pelo')], max_length=10, null=True, verbose_name='tipo de Pelo'),
        ),
        migrations.AddField(
            model_name='mascotas',
            name='tratamiento',
            field=models.CharField(blank=True, choices=[('Si', 'Si'), ('No', 'No')], max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name='descripcion_mascota',
        ),
    ]
