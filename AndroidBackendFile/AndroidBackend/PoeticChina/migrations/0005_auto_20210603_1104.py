# Generated by Django 3.0.6 on 2021-06-03 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PoeticChina', '0004_auto_20210603_0853'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poem',
            old_name='poem_name',
            new_name='name',
        ),
        migrations.AlterModelTable(
            name='poem',
            table='poem',
        ),
        migrations.AlterModelTable(
            name='poet',
            table='poet',
        ),
    ]
