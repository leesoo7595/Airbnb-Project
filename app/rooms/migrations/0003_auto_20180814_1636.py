# Generated by Django 2.1 on 2018-08-14 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_auto_20180814_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomreservation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='roomreservation',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
