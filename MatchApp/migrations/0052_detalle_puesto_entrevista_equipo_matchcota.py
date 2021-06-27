# Generated by Django 3.1.7 on 2021-05-04 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MatchApp', '0051_auto_20210321_2149'),
    ]

    operations = [
        migrations.CreateModel(
            name='detalle_puesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puesto', models.CharField(blank=True, max_length=254, null=True, verbose_name='Puesto')),
            ],
        ),
        migrations.CreateModel(
            name='equipo_matchcota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=254, null=True, verbose_name='Nombre')),
                ('condicion', models.CharField(blank=True, choices=[('Voluntario', 'Voluntario'), ('Staff permanente', 'Staff permanente'), ('Fundador', 'Fundador'), ('Contratado', 'Contratado'), ('Fundador/Staff permanente', 'Fundador/Staff permanente')], max_length=50, null=True, verbose_name='Condicion')),
                ('dni', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=254, null=True, verbose_name='email Personal')),
                ('email_matchcota', models.CharField(blank=True, max_length=254, null=True, verbose_name='email_Matchcota')),
                ('tel_celular', models.CharField(blank=True, max_length=100, null=True, verbose_name='Telefono celular')),
                ('f_nacimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento')),
                ('nacionalidad', models.CharField(blank=True, max_length=10, null=True, verbose_name='telefono fijo')),
                ('direccion', models.CharField(blank=True, max_length=200, null=True, verbose_name='Direccion')),
                ('estudios_cursados', models.CharField(blank=True, max_length=100, null=True, verbose_name='Estudios')),
                ('ocupacion', models.CharField(blank=True, max_length=50, null=True, verbose_name='Ocupacion')),
                ('empresa', models.CharField(blank=True, max_length=100, null=True, verbose_name='Empresa')),
                ('t_coche', models.CharField(blank=True, choices=[('Si', 'Si'), ('No', 'No'), ('N/A', 'N/A')], max_length=20, null=True, verbose_name='Tiene coche')),
                ('visito_albergue', models.CharField(blank=True, choices=[('Si', 'Si'), ('No', 'No'), ('N/A', 'N/A')], max_length=20, null=True, verbose_name='Visito Albergue')),
                ('f_ingreso', models.DateField(blank=True, null=True, verbose_name='Fecha de Ingreso')),
                ('f_cese', models.DateField(blank=True, null=True, verbose_name='Fecha de Cese')),
                ('id_detalle_puesto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MatchApp.detalle_puesto', verbose_name='Puesto')),
                ('id_distrito', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MatchApp.distrito', verbose_name='Distrito')),
            ],
        ),
        migrations.CreateModel(
            name='entrevista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_entrevista', models.DateField(blank=True, null=True, verbose_name='Fecha de Entrevista')),
                ('resultado', models.CharField(blank=True, choices=[('Aprobado', 'Aprobado'), ('No Aprobado', 'No Aprobado')], max_length=15, null=True, verbose_name='Resultado')),
                ('puntuacion', models.CharField(blank=True, choices=[('N/A', 'N/A'), ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=3, null=True, verbose_name='Puntuacion')),
                ('Comentarios_entrevista', models.CharField(blank=True, max_length=100, null=True, verbose_name='Comentarios')),
                ('id_equipo_matchcota', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MatchApp.equipo_matchcota', verbose_name='Entrevistador')),
                ('id_mascotas', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MatchApp.mascotas', verbose_name='Mascota')),
                ('id_persona', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MatchApp.persona', verbose_name='Entrevistado')),
            ],
        ),
    ]
