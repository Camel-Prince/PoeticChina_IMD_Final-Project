# Generated by Django 3.0.6 on 2021-06-28 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PoeticChina', '0008_auto_20210608_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='poem',
            name='poem_img',
            field=models.CharField(default='', max_length=500, verbose_name='img'),
        ),
    ]