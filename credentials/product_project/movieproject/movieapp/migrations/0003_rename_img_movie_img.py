# Generated by Django 4.1.4 on 2022-12-31 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_movie_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='img',
            new_name='Img',
        ),
    ]
