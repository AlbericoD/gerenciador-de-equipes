# Generated by Django 2.2.7 on 2019-11-11 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treinador', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='treinador',
            old_name='aniversario',
            new_name='nascimento',
        ),
    ]