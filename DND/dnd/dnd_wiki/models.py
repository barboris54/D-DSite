from django.db import models


class HeroesClass(models.Model):
    rus_name = models.CharField(max_length=200)
    eng_name = models.CharField(max_length=200)
    adons_name = models.CharField(max_length=200)
    bg_image = models.ImageField(upload_to='dnd_wiki/icons', default='')

    def __str__(self):
        return self.rus_name
