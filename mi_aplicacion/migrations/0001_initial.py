# Generated by Django 4.2.8 on 2023-12-21 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GPS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imei', models.CharField(max_length=20)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('alt', models.FloatField()),
                ('speed', models.FloatField()),
                ('orientation', models.FloatField()),
                ('acc', models.IntegerField()),
                ('di1', models.IntegerField()),
                ('towing', models.IntegerField()),
            ],
        ),
    ]