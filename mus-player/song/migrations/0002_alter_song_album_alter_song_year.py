# Generated by Django 4.0.5 on 2022-06-06 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='song',
            name='year',
            field=models.IntegerField(blank=True),
        ),
    ]
