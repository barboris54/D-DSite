from django.shortcuts import render
from .models import HeroesClass, BardSpells, Races,RaceQualities,Spell
from django.db.models import Q

def main_page(request):
    pr = HeroesClass.objects.all()
    context = {'heroes': pr}
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

def spells(request):
    search_query=''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    sp = Spell.objects.filter(Q(name__icontains=search_query) | Q(lvl__icontains=search_query))
    context = {'spells': sp, 'search_query': search_query}
    return render(request,'dnd_wiki/spells.html', context)

def single_spell(request, pk):
    spell_obj = Spell.objects.get(id=pk)
    spells = Spell.objects.all()
    context = {'so': spell_obj, 'spells': spells}
    return render(request, 'dnd_wiki/spell_description.html', context)