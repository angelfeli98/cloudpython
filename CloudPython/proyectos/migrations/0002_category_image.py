# Generated by Django 3.0.6 on 2020-06-06 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='null', upload_to='Categories'),
        ),
    ]
