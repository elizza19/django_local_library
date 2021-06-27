# Generated by Django 3.1.7 on 2021-05-16 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_color', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='detalle_puesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puesto', models.CharField(blank=True, max_length=254, null=True, verbose_name='Puesto')),
            ],
        ),
        migrations.CreateModel(
            name='distrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_postal', models.CharField(blank=True, max_length=30, null=True)),
                ('nombre_distrito', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='medio_contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='tipo_mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='albergues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_albergue', models.CharField(blank=True, max_length=50, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=30, null=True)),
                ('direccion', models.CharField(blank=True, max_length=1000, null=True)),
                ('referencia', models.CharField(blank=True, max_length=11000, null=True)),
                ('duena', models.CharField(blank=True, max_length=100, null=True)),
                ('responsable', models.CharField(blank=True, max_length=100, null=True)),
                ('cuidador', models.CharField(blank=True, max_length=100, null=True)),
                ('dias_atencion', models.CharField(blank=True, max_length=100, null=True)),
                ('horario_atencion', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_ingreso_matchcota', models.DateField(blank=True, null=True)),
                ('vigente', models.CharField(blank=True, max_length=2, null=True)),
                ('id_distrito', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mantenimientoApp.distrito')),
            ],
        ),
    ]