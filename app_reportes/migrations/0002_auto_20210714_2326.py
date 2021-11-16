# Generated by Django 3.1.7 on 2021-07-15 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_reportes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservas',
            name='duracion_masaje',
            field=models.CharField(default='30min', max_length=10),
        ),
        migrations.AlterField(
            model_name='masaje',
            name='duracion_masaje',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='reservas',
            name='inactiva',
            field=models.BooleanField(default=False, verbose_name='históricas'),
        ),
    ]