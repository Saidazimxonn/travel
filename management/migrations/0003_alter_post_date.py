# Generated by Django 3.2.9 on 2022-06-06 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20220407_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
