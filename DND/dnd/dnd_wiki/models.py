from django.db import models


class HeroesClass(models.Model):
    rus_name = models.CharField(max_length=200)
    eng_name = models.CharField(max_length=200)
    adons_name = models.CharField(max_length=200)
    bg_image = models.ImageField(upload_to='dnd_wiki/icons', default='', blank=True)
    name = models.CharField(max_length=200, default="default title")
    source = models.CharField(max_length=200, default="default title")
    lore_info = models.TextField(null=True, blank=True, default="default title")
    short_info = models.CharField(max_length=200, default="default title")
    table = models.TextField(null=True, blank=True, default="default title")
    description_title1 = models.CharField(max_length=200, null=True, blank=True, default="default title")
    description_info1 = models.TextField(null=True, blank=True, default="default title")
    description_title2 = models.CharField(max_length=200, null=True, blank=True, default="default title")
    description_info2 = models.TextField(null=True, blank=True, default="default title")
    fast_creations = models.TextField(null=True, blank=True, default="default title")
    creations = models.TextField(default="default title")
    deep_lore_decs = models.CharField(null=True, blank=True, default="default title", max_length=200)
    deep_lore_min_char = models.CharField(null=True, blank=True, default="default title", max_length=200)
    deep_lore_use = models.CharField(null=True, blank=True, default="default title", max_length=200)
    deep_lore_ability = models.CharField(null=True, blank=True, default="default title", max_length=200)
    class_ability_desc = models.CharField(null=True, blank=True, default="default title", max_length=200)
    class_ability_hp = models.CharField(null=True, blank=True, default="default title", max_length=200)
    class_ability_hp_1lvl = models.CharField(null=True, blank=True, default="default title", max_length=200)
    class_ability_hp_nextlvl = models.CharField(null=True, blank=True, default="default title", max_length=200)
    class_ability_armor = models.CharField(null=True, blank=True, default="default title", max_length=200)
    class_ability_weapon = models.CharField(null=True, blank=True, default="default title", max_length=200)
    class_ability_tools = models.CharField(null=True, blank=True, default="default title", max_length=200)
    class_ability_safedice = models.CharField(null=True, blank=True, default="default title", max_length=200)
    class_ability_equipment1 = models.CharField(null=True, blank=True, default="default title", max_length=200)
    class_ability_equipment2 = models.CharField(null=True, blank=True, default="default title", max_length=200)
    class_ability_equipment3 = models.CharField(null=True, blank=True, default="default title", max_length=200)
    # законичл классовые умения
    spell_using = models.CharField(null=True, blank=True, default="default title", max_length=200)
    spell_using_decs = models.TextField(null=True, blank=True, default="default title")
    extra_spell = models.CharField(null=True, blank=True, default="default title", max_length=200)
    extra_spell_table = models.TextField(null=True, blank=True, default="default title")

    def __str__(self):
        return self.rus_name




class Races(models.Model):
    rus_name = models.CharField(max_length=200)
    eng_name = models.CharField(max_length=200)
    adons_name = models.CharField(max_length=200)
    bg_image = models.ImageField(upload_to='dnd_wiki/icons', default='', blank=True)
    description = models.TextField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    male_names = models.TextField(blank=True, null=True)
    female_names = models.TextField(blank=True, null=True)
    race_qualites = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.rus_name


class BardSpells(models.Model):
    hero_class = models.ForeignKey(HeroesClass, on_delete=models.PROTECT)
    hero_class_str = models.CharField(null=True, blank=True, default="default title", max_length=200)
    title = models.CharField(null=True, blank=True, default="default title", max_length=200)
    description_spell = models.TextField(null=True, blank=True, default="default title")
    lvl = models.CharField(null=True, blank=True, default="default title", max_length=200)
    def __str__(self):
        return self.hero_class_str


class RaceQualities(models.Model):
    race = models.CharField(null=True, blank=True, default="default title", max_length=200)
    title = models.CharField(null=True, blank=True, default="default title", max_length=200)
    description = models.TextField(null=True, blank=True, default="default title")
    def __str__(self):
        return self.race

class Spell(models.Model):
    name = models.CharField(null=True, blank=True, default="default title", max_length=200)
    lvl = models.CharField(null=True, blank=True, default="default title", max_length=200)
    companent = models.CharField(null=True, blank=True, default="default title", max_length=200)
    description = models.TextField(null=True, blank=True, default="default title")
    def __str__(self):
        return self.name

