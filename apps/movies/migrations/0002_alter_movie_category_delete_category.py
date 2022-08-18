# Generated by Django 4.1 on 2022-08-17 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.category', verbose_name='Категория'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
