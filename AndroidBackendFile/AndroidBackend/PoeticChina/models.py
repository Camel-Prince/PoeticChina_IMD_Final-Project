from django.db import models
from Login import *

# Create your models here.
from Login.models import Login


class Poet(models.Model):
    name = models.CharField('name', max_length=50, default='')
    introduction = models.TextField('intro', default=' ')
    poet_img = models.CharField('img', max_length=500, default='')

    class Meta:
        db_table = "poet"


class Poem(models.Model):
    name = models.CharField('name', max_length=50, default='')
    content = models.TextField('content', default=' ')
    analysis = models.TextField('analysis', default='')
    poet = models.ForeignKey(Poet, on_delete=models.CASCADE)
    poem_img = models.CharField('img', max_length=500, default='')
    time = models.CharField('time', max_length=10, default="$tang$")

    class Meta:
        db_table = "poem"


class Poem_Theme(models.Model):
    poem = models.ForeignKey(Poem, on_delete=models.CASCADE)
    theme = models.CharField('theme', max_length=50, default='未分类')

    class Meta:
        db_table = 'poem_theme'
        unique_together = ('poem_id', 'theme')


class Collect(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    poem = models.ForeignKey(Poem, on_delete=models.CASCADE)

    class Meta:
        db_table = 'collect'
