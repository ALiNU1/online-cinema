# Generated by Django 4.1 on 2022-08-19 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_remove_movie_actors_remove_movie_directors_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='directors',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='film_director', to='movies.directors', verbose_name='режиссер'),
        ),
    ]
