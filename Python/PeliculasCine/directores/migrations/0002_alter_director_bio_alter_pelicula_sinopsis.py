# Generated by Django 4.2 on 2023-04-18 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='bio',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='sinopsis',
            field=models.TextField(max_length=2000),
        ),
    ]
