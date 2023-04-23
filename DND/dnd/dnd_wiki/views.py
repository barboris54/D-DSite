from django.shortcuts import render


def main_page(request):
    return render(request, 'dnd_wiki/main_page.html')
