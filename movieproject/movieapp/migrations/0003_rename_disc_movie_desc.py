# Generated by Django 4.2 on 2023-05-01 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_movie_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='disc',
            new_name='desc',
        ),
    ]
