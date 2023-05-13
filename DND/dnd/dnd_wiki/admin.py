from django.contrib import admin
from .models import HeroesClass, Companions, ClassHomebrew, BardSpells

admin.site.register(HeroesClass)
admin.site.register(Companions)
admin.site.register(ClassHomebrew)
admin.site.register(BardSpells)
