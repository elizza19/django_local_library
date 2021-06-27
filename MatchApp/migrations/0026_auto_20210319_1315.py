# Generated by Django 3.1.7 on 2021-03-19 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MatchApp', '0025_auto_20210319_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascotas',
            name='amigable',
            field=models.CharField(blank=True, choices=[('N/A', 'N/A'), ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='mascotas',
            name='carinoso',
            field=models.CharField(blank=True, choices=[('N/A', 'N/A'), ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='mascotas',
            name='curioso',
            field=models.CharField(blank=True, choices=[('N/A', 'N/A'), ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='mascotas',
            name='deportista',
            field=models.CharField(blank=True, choices=[('N/A', 'N/A'), ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='mascotas',
            name='dominante',
            field=models.CharField(blank=True, choices=[('N/A', 'N/A'), ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='mascotas',
            name='educado',
            field=models.CharField(blank=True, choices=[('N/A', 'N/A'), ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='mascotas',
            name='extrovertido',
            field=models.CharField(blank=True, choices=[('N/A', 'N/A'), ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='mascotas',
            name='impulsivo',
            field=models.CharField(blank=True, choices=[('N/A', 'N/A'), ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='mascotas',
            name='independiente',
            field=models.CharField(blank=True, choices=[('N/A', 'N/A'), ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='mascotas',
            name='jugueton',
            field=models.CharField(blank=True, choices=[('N/A', 'N/A'), ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='mascotas',
            name='temeroso',
            field=models.CharField(blank=True, choices=[('N/A', 'N/A'), ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='mascotas',
            name='tranquilo',
            field=models.CharField(blank=True, choices=[('N/A', 'N/A'), ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=3, null=True),
        ),
    ]
