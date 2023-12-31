# Generated by Django 4.2.8 on 2023-12-21 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mi_aplicacion', '0002_gps_sensores'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc', models.IntegerField()),
                ('di1', models.IntegerField()),
                ('towing', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='gps',
            name='acc',
        ),
        migrations.RemoveField(
            model_name='gps',
            name='di1',
        ),
        migrations.RemoveField(
            model_name='gps',
            name='towing',
        ),
        migrations.AlterField(
            model_name='gps',
            name='sensores',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='mi_aplicacion.sensores'),
        ),
    ]
