from random import randint
from django.shortcuts import render, redirect
from django.views import View
from gameplay_app.models import MazeHero, Maze
from hero_app.models import Hero
from monster_app.models import Monster
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin


class EntryMazeView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):
        if request.session.get('actual_hero') is None:
            return redirect(reverse('hero_list'))

        hero = request.session.get('actual_hero')
        hero = Hero.objects.get(id=hero)

        actual_position = MazeHero.objects.get(hero_id=hero.id, active_position=True)
        actual_position = Maze.objects.get(position=actual_position.position)

        if actual_position.position > 1:

            return redirect(reverse('maze', kwargs={'slug': actual_position.slug}))

        return render(request, 'maze_entry.html', context={
            'hero': hero,
        })


class MazeMovementView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request, slug):


        return render(request, 'maze.html', )


class MazeIntroFightView(View):

    def get(self, request, slug):
        pass
