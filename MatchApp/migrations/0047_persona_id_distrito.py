# Generated by Django 3.1.7 on 2021-03-21 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MatchApp', '0046_persona_direccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='id_distrito',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MatchApp.distrito', verbose_name='Distrito'),
        ),
    ]
