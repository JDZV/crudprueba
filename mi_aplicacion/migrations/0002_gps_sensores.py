# Generated by Django 4.2.8 on 2023-12-21 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gps',
            name='sensores',
            field=models.CharField(default='default_value', max_length=100),
        ),
    ]
