# Generated by Django 2.0.8 on 2018-10-19 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_movie_otkliks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='otkliks',
        ),
    ]