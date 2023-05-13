from django.shortcuts import render
from .models import HeroesClass, Companions, ClassHomebrew, BardSpells

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
    return render(request, 'dnd_wiki/race.html')