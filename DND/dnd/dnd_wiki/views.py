from django.shortcuts import render
from .models import HeroesClass

def main_page(request):
    pr = HeroesClass.objects.all()
    context = {'heroes': pr}
    return render(request, 'dnd_wiki/main_page.html', context)
