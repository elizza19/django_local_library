# Generated by Django 3.1.7 on 2021-03-19 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MatchApp', '0023_auto_20210318_2056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalidad_perro',
            name='id_mascota',
        ),
        migrations.AddField(
            model_name='mascotas',
            name='amigable',
            field=models.CharField(blank=True, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='mascotas',
            name='carinoso',
            field=models.CharField(blank=True, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='mascotas',
            name='curioso',
            field=models.CharField(blank=True, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='mascotas',
            name='deportista',
            field=models.CharField(blank=True, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='mascotas',
            name='dominante',
            field=models.CharField(blank=True, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='mascotas',
            name='educado',
            field=models.CharField(blank=True, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='mascotas',
            name='extrovertido',
            field=models.CharField(blank=True, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='mascotas',
            name='impulsivo',
            field=models.CharField(blank=True, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='mascotas',
            name='independiente',
            field=models.CharField(blank=True, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='mascotas',
            name='jugueton',
            field=models.CharField(blank=True, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='mascotas',
            name='relacion_p_hembras',
            field=models.CharField(blank=True, choices=[('S', 'Si'), ('N', 'No')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='mascotas',
            name='relacion_p_humanos',
            field=models.CharField(blank=True, choices=[('S', 'Si'), ('N', 'No')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='mascotas',
            name='relacion_p_machos',
            field=models.CharField(blank=True, choices=[('S', 'Si'), ('N', 'No')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='mascotas',
            name='sociable_humanos',
            field=models.CharField(blank=True, choices=[('S', 'Si'), ('N', 'No')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='mascotas',
            name='temeroso',
            field=models.CharField(blank=True, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='mascotas',
            name='tranquilo',
            field=models.CharField(blank=True, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='mascotas',
            name='activo_web',
            field=models.CharField(blank=True, choices=[('S', 'Si'), ('N', 'No')], max_length=20, null=True, verbose_name='Activo en Web'),
        ),
        migrations.AlterField(
            model_name='mascotas',
            name='alergias',
            field=models.CharField(blank=True, choices=[('S', 'Si'), ('N', 'No')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='mascotas',
            name='enfermedad_cronica',
            field=models.CharField(blank=True, choices=[('S', 'Si'), ('N', 'No')], max_length=20, null=True, verbose_name='enfermedad cronica'),
        ),
        migrations.AlterField(
            model_name='mascotas',
            name='esterilizado',
            field=models.CharField(blank=True, choices=[('S', 'Si'), ('N', 'No')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='mascotas',
            name='numero_carnet',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Numero Carnet'),
        ),
        migrations.AlterField(
            model_name='mascotas',
            name='tratamiento',
            field=models.CharField(blank=True, choices=[('S', 'Si'), ('N', 'No')], max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name='personalidad_gato',
        ),
        migrations.DeleteModel(
            name='personalidad_perro',
        ),
    ]
