# Generated by Django 3.0.6 on 2020-06-07 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0005_auto_20200607_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyect',
            name='deadline',
            field=models.DateField(),
        ),
    ]
