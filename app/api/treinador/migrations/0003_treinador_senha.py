# Generated by Django 2.2.7 on 2019-11-11 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treinador', '0002_auto_20191111_0522'),
    ]

    operations = [
        migrations.AddField(
            model_name='treinador',
            name='senha',
            field=models.CharField(default='', max_length=255),
        ),
    ]
