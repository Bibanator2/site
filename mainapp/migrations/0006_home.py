# Generated by Django 4.2.4 on 2023-08-19 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_rename_сon_data_artline'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('anons', models.CharField(max_length=200, verbose_name='Анонс')),
                ('full_text', models.TextField(verbose_name='Описание')),
            ],
        ),
    ]
