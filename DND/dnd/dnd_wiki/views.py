from django.shortcuts import render
from .models import HeroesClass, Companions, ClassHomebrew

def main_page(request):
    pr = HeroesClass.objects.all()
    comp = Companions.objects.all()
    hb = ClassHomebrew.objects.all()
    context = {'heroes': pr, 'companions':comp, 'hb_heroes': hb}
    return render(request, 'dnd_wiki/main_page.html', context)

def single_class(request, pk):
    hero_obj = HeroesClass.objects.get(id=pk)
    return render(request, 'dnd_wiki/single_class.html', {'ho': hero_obj})