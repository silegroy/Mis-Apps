# Generated by Django 3.1.7 on 2021-07-05 20:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Masaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tratamiento', models.CharField(max_length=100)),
                ('duracion_masaje', models.CharField(choices=[('30 min', '30 MIN'), ('45 min', '45 MIN'), ('75 min', '75 MIN')], max_length=50)),
            ],
            options={
                'verbose_name': 'Masaje',
                'verbose_name_plural': 'Masajes',
                'db_table': 'Masaje',
                'ordering': ['nombre_tratamiento'],
            },
        ),
        migrations.CreateModel(
            name='Masajista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_masajista', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Masajista',
                'verbose_name_plural': 'Masajistas',
                'db_table': 'Masajista',
                'ordering': ['nombre_masajista'],
            },
        ),
        migrations.CreateModel(
            name='Reservas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habitacion_cliente', models.IntegerField()),
                ('nombre_cliente', models.CharField(max_length=100)),
                ('fecha_reserva', models.DateField(default=datetime.datetime.now)),
                ('fecha_a_reservar', models.DateField()),
                ('hora_reserva', models.TimeField()),
                ('activa', models.BooleanField(default=True)),
                ('inactiva', models.BooleanField(default=True)),
                ('cancelada', models.BooleanField(default=False)),
                ('observaciones', models.TextField(blank=True, max_length=300)),
                ('nombre_masajista', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_reportes.masajista')),
                ('nombre_tratamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_reportes.masaje')),
                ('quien_realiza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Reserva',
                'verbose_name_plural': 'Reservas',
                'db_table': 'Reserva',
                'ordering': ['-fecha_a_reservar'],
            },
        ),
    ]
