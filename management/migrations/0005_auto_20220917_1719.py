# Generated by Django 3.2.9 on 2022-09-17 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_alter_media_fiel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livemessage',
            name='message_long',
            field=models.TextField(verbose_name='Matin '),
        ),
        migrations.AlterField(
            model_name='livemessage',
            name='message_long_en',
            field=models.TextField(null=True, verbose_name='Matin '),
        ),
        migrations.AlterField(
            model_name='livemessage',
            name='message_long_ru',
            field=models.TextField(null=True, verbose_name='Matin '),
        ),
        migrations.AlterField(
            model_name='livemessage',
            name='message_long_uz',
            field=models.TextField(null=True, verbose_name='Matin '),
        ),
    ]
