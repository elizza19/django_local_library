# Generated by Django 3.1.7 on 2021-03-14 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MatchApp', '0012_auto_20210314_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascotas',
            name='tipo',
            field=models.CharField(blank=True, choices=[('P', 'Perro'), ('G', 'Gato')], max_length=10, null=True),
        ),
    ]
