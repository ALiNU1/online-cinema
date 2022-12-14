from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название сайта')),
                ('description', models.TextField(verbose_name='Описание сайта')),
                ('logo', models.ImageField(upload_to='logo/', verbose_name='Логотип сайта')),
                ('phone', models.CharField(max_length=255, verbose_name='Телефонный номер')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('email', models.EmailField(max_length=150, verbose_name='Электронная почта сайта')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Ссылка на facebook')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Ссылка на twitter')),
                ('youtube', models.URLField(blank=True, null=True, verbose_name='Ссылка на youtube')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Ссылка на instagram')),
                ('linkedin', models.URLField(blank=True, null=True, verbose_name='Ссылка на linkedin')),
            ],
            options={
                'verbose_name': 'Настройка',
                'verbose_name_plural': 'Настройки',
            },
        ),
    ]
