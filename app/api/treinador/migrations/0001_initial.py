# Generated by Django 2.2.7 on 2019-11-11 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Treinador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('aniversario', models.DateField()),
                ('detalhes', models.TextField()),
                ('credencial', models.IntegerField()),
                ('esportes_capacitados', models.CharField(choices=[('Futebol', 'Futebol'), ('Volei', 'Volei'), ('Natacao', 'Natação'), ('Luta', 'Luta')], default='Futebol', max_length=10)),
            ],
        ),
    ]
