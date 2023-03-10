# Generated by Django 4.1.6 on 2023-02-04 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rev_date', models.DateTimeField(auto_now_add=True)),
                ('temp', models.IntegerField()),
                ('humi', models.IntegerField()),
                ('light', models.IntegerField()),
                ('rain', models.IntegerField()),
                ('water', models.IntegerField()),
            ],
        ),
    ]
