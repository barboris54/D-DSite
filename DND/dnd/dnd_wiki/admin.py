from django.contrib import admin
from .models import HeroesClass, Companions, ClassHomebrew, BardSpells, Races, RaceQualities, Spell

admin.site.register(HeroesClass)
admin.site.register(Companions)
admin.site.register(ClassHomebrew)
admin.site.register(BardSpells)
admin.site.register(Races)
admin.site.register(RaceQualities)
admin.site.register(Spell)

