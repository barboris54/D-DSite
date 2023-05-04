from django.db import models


class HeroesClass(models.Model):
    rus_name = models.CharField(max_length=200)
    eng_name = models.CharField(max_length=200)
    adons_name = models.CharField(max_length=200)
    bg_image = models.ImageField(upload_to='dnd_wiki/icons', default='', blank=True)

    def __str__(self):
        return self.rus_name

class Companions(models.Model):
    rus_name = models.CharField(max_length=200)
    eng_name = models.CharField(max_length=200)
    adons_name = models.CharField(max_length=200)
    bg_image = models.ImageField(upload_to='dnd_wiki/icons', default='', blank=True)

    def __str__(self):
        return self.rus_name

class ClassHomebrew(models.Model):
    rus_name = models.CharField(max_length=200)
    eng_name = models.CharField(max_length=200)
    adons_name1 = models.CharField(max_length=200)
    adons_name2 = models.CharField(max_length=200, blank=True)
    adons_name3 = models.CharField(max_length=200, blank=True)
    bg_image = models.ImageField(upload_to='dnd_wiki/icons', default='', blank=True)