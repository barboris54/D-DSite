from django.shortcuts import render
from .models import HeroesClass, Companions, ClassHomebrew, BardSpells, Races,RaceQualities

def main_page(request):
    pr = HeroesClass.objects.all()
    comp = Companions.objects.all()
    hb = ClassHomebrew.objects.all()
    context = {'heroes': pr, 'companions':comp, 'hb_heroes': hb}
    return render(request, 'dnd_wiki/main_page.html', context)

def single_class(request, pk):
    hero_obj = HeroesClass.objects.get(id=pk)
    bard_spells = BardSpells.objects.all()
    context = {'ho': hero_obj, 'bs': bard_spells}
    return render(request, 'dnd_wiki/single_class.html', context)

def race(request):
    races = Races.objects.all()
    context = {'races': races}
    return render(request, 'dnd_wiki/race.html', context)

def single_race(request, pk):
    race_obj = Races.objects.get(id=pk)
    race_qualities = RaceQualities.objects.all()
    context = {'ro': race_obj, 'rq': race_qualities}
    return render(request, 'dnd_wiki/single_race.html', context)