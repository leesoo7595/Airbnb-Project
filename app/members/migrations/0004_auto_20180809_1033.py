# Generated by Django 2.1 on 2018-08-09 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20180808_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=50),
        ),
    ]
