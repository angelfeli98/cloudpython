# Generated by Django 3.0.6 on 2020-06-06 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0003_auto_20200606_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyect',
            name='deadline',
            field=models.DateField(),
        ),
    ]
