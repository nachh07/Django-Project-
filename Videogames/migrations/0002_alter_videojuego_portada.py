# Generated by Django 4.1.1 on 2022-11-21 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Videogames', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videojuego',
            name='portada',
            field=models.ImageField(blank=True, null=True, upload_to='videojuegos'),
        ),
    ]
