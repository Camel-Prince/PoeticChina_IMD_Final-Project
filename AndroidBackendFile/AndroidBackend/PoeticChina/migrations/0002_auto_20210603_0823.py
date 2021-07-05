# Generated by Django 3.0.6 on 2021-06-03 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PoeticChina', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poem_name', models.CharField(default='', max_length=50, verbose_name='name')),
                ('theme', models.CharField(default='', max_length=50, verbose_name='theme')),
            ],
        ),
        migrations.CreateModel(
            name='Poet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, verbose_name='name')),
                ('introduction', models.CharField(max_length=1000, verbose_name='intro')),
            ],
        ),
        migrations.DeleteModel(
            name='Poems',
        ),
        migrations.AddField(
            model_name='poem',
            name='poet_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PoeticChina.Poet'),
        ),
    ]
