# Generated by Django 4.2.4 on 2023-08-18 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='anons',
            field=models.CharField(max_length=250, null=True, verbose_name='Анонс'),
        ),
        migrations.AlterField(
            model_name='file',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Заголовок'),
        ),
    ]
