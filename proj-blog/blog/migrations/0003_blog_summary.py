# Generated by Django 4.0.4 on 2022-06-06 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_content_alter_blog_photo_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='summary',
            field=models.TextField(blank=True),
        ),
    ]
