# Generated by Django 4.1 on 2022-08-24 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0012_alter_movie_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='url',
            field=models.SlugField(max_length=130, unique=True),
        ),
    ]
