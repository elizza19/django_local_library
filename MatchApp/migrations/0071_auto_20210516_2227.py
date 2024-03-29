# Generated by Django 3.1.7 on 2021-05-16 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Equipo_MatchcotaApp', '0001_initial'),
        ('MatchApp', '0070_auto_20210516_2202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipo_matchcota',
            name='id_detalle_puesto',
        ),
        migrations.RemoveField(
            model_name='equipo_matchcota',
            name='id_distrito',
        ),
        migrations.AlterField(
            model_name='adopciones',
            name='id_etologo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='id_etologo+', to='Equipo_MatchcotaApp.equipo_matchcota', verbose_name='Resp Regul.'),
        ),
        migrations.AlterField(
            model_name='adopciones',
            name='resp_adopcion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resp_adopcion+', to='Equipo_MatchcotaApp.equipo_matchcota', verbose_name='Resp Adopcion'),
        ),
        migrations.AlterField(
            model_name='adopciones',
            name='resp_regularizacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resp_regularizacion+', to='Equipo_MatchcotaApp.equipo_matchcota', verbose_name='Resp Regul.'),
        ),
        migrations.AlterField(
            model_name='entrevista',
            name='id_equipo_matchcota',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Equipo_MatchcotaApp.equipo_matchcota', verbose_name='Entrevistador'),
        ),
        migrations.DeleteModel(
            name='detalle_puesto',
        ),
        migrations.DeleteModel(
            name='equipo_matchcota',
        ),
    ]
