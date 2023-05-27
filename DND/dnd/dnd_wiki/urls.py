from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('class_description/<str:pk>', views.single_class, name='single_class'),
    path('race/', views.race, name='race'),
    path('race_description/<str:pk>', views.single_race, name='single_race'),
    path('spells/', views.spells, name='spells'),
    path('spells_description/<str:pk>', views.single_spell, name='single_spell'),

]