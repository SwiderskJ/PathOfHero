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
        actual_position = Maze.objects.get(position=actual_position.position.position)

        if actual_position.position > 1:

            return redirect(reverse('maze', kwargs={'slug': actual_position.slug}))

        return render(request, 'maze_entry.html', context={
            'hero': hero,
        })


class MazeMovementView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request, slug):
        maze = Maze.objects.get(slug=slug)
        return render(request, 'maze.html', context={
            "maze": maze,
        })


class MazeIntroFightView(View):

    def get(self, request, slug):
        hero = request.session.get('actual_hero')
        hero = Hero.objects.get(id=hero)
        maze = Maze.objects.get(slug=slug)
        random_number = randint(1, 10)
        random_number_two = randint(0, 3)
        random_number = random_number + maze.difficulty

        if random_number > 10:
            random_number = 10

        if random_number < 1:
            random_number = 1

        monster = Monster.objects.filter(difficult=random_number)
        monster_count = monster.count()
        monster_count = randint(1, monster_count)
        monster = monster[monster_count - 1]
        if random_number in [7, 8, 9, 10]:
            messages = "Should be easy"
        if random_number in [4, 5, 6]:
            messages = "Maybe you win"
        if random_number in [2, 3]:
            messages = "The strongest and most powerful enemies"
        if random_number in [1]:
            messages = "Only for true heroes"

        return render(request, 'maze_pre_fight.html', context={
            'hero': hero,
            'message': messages,
            'monster': monster,
        })


class FightView(View):

    def get(self, request, slug):
        pass
