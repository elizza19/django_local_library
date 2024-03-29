# Generated by Django 3.1.7 on 2021-05-09 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MatchApp', '0057_auto_20210509_0046'),
    ]

    operations = [
        migrations.CreateModel(
            name='adopciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_adoptado', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre Adoptado')),
                ('tipo', models.CharField(blank=True, choices=[('Adopción', 'Adopción'), ('Intento', 'Intento')], max_length=20, null=True, verbose_name='Tipo')),
                ('f_adopcion', models.DateField(blank=True, null=True, verbose_name='Fecha de Adopcion')),
                ('riesgo_asociado', models.CharField(blank=True, choices=[('Alto', 'Alto'), ('Medio', 'Medio'), ('Bajo', 'Bajo')], max_length=20, null=True, verbose_name='Nivel de riesgo')),
                ('motivo_riesgo', models.CharField(blank=True, max_length=5000, null=True, verbose_name='Motivo de Riesgo')),
                ('doc_regularizada', models.CharField(blank=True, choices=[('Si', 'Si'), ('No', 'No'), ('N/A', 'N/A')], max_length=20, null=True, verbose_name='Doc. Regularizada')),
                ('f_regularizacion', models.DateField(blank=True, null=True, verbose_name='Fecha de Adopcion')),
                ('req_etologo', models.CharField(blank=True, choices=[('Si', 'Si'), ('No', 'No'), ('N/A', 'N/A')], max_length=20, null=True, verbose_name='Requiere Estologo')),
                ('comentario', models.CharField(blank=True, max_length=5000, null=True, verbose_name='Comentario')),
                ('intento_dev', models.DateField(blank=True, null=True, verbose_name='Fecha Int. Dev')),
                ('concluida', models.CharField(blank=True, choices=[('Si', 'Si'), ('No', 'No'), ('N/A', 'N/A')], max_length=20, null=True, verbose_name='Concluida')),
                ('id_entrevista', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MatchApp.entrevista', verbose_name='Entrevista')),
                ('id_etologo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='id_etologo+', to='MatchApp.equipo_matchcota', verbose_name='Resp Regul.')),
                ('resp_adopcion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resp_adopcion+', to='MatchApp.equipo_matchcota', verbose_name='Resp Adopcion')),
                ('resp_regularizacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resp_regularizacion+', to='MatchApp.equipo_matchcota', verbose_name='Resp Regul.')),
            ],
        ),
    ]
