# Generated by Django 3.0.6 on 2021-07-03 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PoeticChina', '0010_poem_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='poet',
            name='poet_img',
            field=models.CharField(default='', max_length=500, verbose_name='img'),
        ),
    ]
