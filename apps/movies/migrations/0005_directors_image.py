# Generated by Django 4.1 on 2022-08-19 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_directors_alter_actor_options_remove_actor_age_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='directors',
            name='image',
            field=models.ImageField(default=1, upload_to='directors/', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]
