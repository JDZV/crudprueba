# Generated by Django 4.2.8 on 2023-12-21 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mi_aplicacion', '0003_sensores_remove_gps_acc_remove_gps_di1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='gps',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='gps',
            name='lon',
        ),
        migrations.AddField(
            model_name='gps',
            name='position',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='mi_aplicacion.position'),
        ),
    ]
