# Generated by Django 3.0.6 on 2020-06-04 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('made', models.DateTimeField(auto_now_add=True)),
                ('upload', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proyect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('goal', models.FloatField()),
                ('actual', models.FloatField()),
                ('description', models.CharField(max_length=1500)),
                ('made', models.DateTimeField(auto_now_add=True)),
                ('upload', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.Category', verbose_name='Category')),
                ('userOwner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Owner', to='usuarios.User', verbose_name='Owner')),
                ('usersPatrons', models.ManyToManyField(to='usuarios.User', verbose_name='Patrons')),
            ],
        ),
    ]
