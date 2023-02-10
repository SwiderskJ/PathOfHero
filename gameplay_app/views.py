from random import randint
from django.shortcuts import render, redirect
from django.views import View
from gameplay_app.models import MazeHero, Maze
from hero_app.models import Hero
from monster_app.models import Monster
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from user_app.models import UserCurrency


class EntryMazeView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):
        if request.session.get('actual_hero') is None:
            return redirect(reverse('hero_list'))

        hero = request.session.get('actual_hero')
        print(hero)
        hero = Hero.objects.get(id=hero)
        print(hero)
        print('*' * 20)
        actual_position = MazeHero.objects.get(hero_id=hero.id, active_position=True)
        actual_position = Maze.objects.get(position=actual_position.position.position)

        if actual_position.position > 1:
            return redirect(reverse('maze'))

        return render(request, 'maze_entry.html', context={
            'hero': hero,
            'maze': actual_position,
        })


class MazeMovementView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):
        hero = request.session.get('actual_hero')
        hero = Hero.objects.get(id=hero)

        actual_position = MazeHero.objects.filter(active_position=True, hero_id=hero.id)
        last_position = actual_position[0].last_position
        actual_position = actual_position[0].position.position
        maze = Maze.objects.get(position=actual_position)

        if maze.events == 3:
            return render(request, 'maze_endpoint.html', context={
                'maze': maze
            })

        if maze.events == 4:
            return render(request, 'boss.html', context={
                'maze': maze,
            })

        if maze.events == 2:
            if actual_position == 4 and last_position == 3:
                left = Maze.objects.get(position=14)
                right = Maze.objects.get(position=5)

                return render(request, 'maze_two_ways.html', context={
                    "right": right,
                    "left": left,
                })
            if actual_position == 4 and last_position == 5:
                left = Maze.objects.get(position=3)
                right = Maze.objects.get(position=14)

                return render(request, 'maze_two_ways.html', context={
                    "right": right,
                    "left": left,
                })
            if actual_position == 4 and last_position == 14:
                left = Maze.objects.get(position=5)
                right = Maze.objects.get(position=3)

                return render(request, 'maze_two_ways.html', context={
                    "right": right,
                    "left": left,
                })
            if actual_position == 6 and last_position == 5:
                left = Maze.objects.get(position=13)
                right = Maze.objects.get(position=7)

                return render(request, 'maze_two_ways.html', context={
                    "right": right,
                    "left": left,
                })
            if actual_position == 6 and last_position == 7:
                left = Maze.objects.get(position=5)
                right = Maze.objects.get(position=13)

                return render(request, 'maze_two_ways.html', context={
                    "right": right,
                    "left": left,
                })
            if actual_position == 6 and last_position == 13:
                left = Maze.objects.get(position=7)
                right = Maze.objects.get(position=5)

                return render(request, 'maze_two_ways.html', context={
                    "right": right,
                    "left": left,
                })
            if actual_position == 20 and last_position == 19:
                left = Maze.objects.get(position=21)
                right = Maze.objects.get(position=22)

                return render(request, 'maze_two_ways.html', context={
                    "right": right,
                    "left": left,
                })
            if actual_position == 20 and last_position == 21:
                left = Maze.objects.get(position=22)
                right = Maze.objects.get(position=19)

                return render(request, 'maze_two_ways.html', context={
                    "right": right,
                    "left": left,
                })
            if actual_position == 20 and last_position == 22:
                left = Maze.objects.get(position=19)
                right = Maze.objects.get(position=21)

                return render(request, 'maze_two_ways.html', context={
                    "right": right,
                    "left": left,
                })
            if actual_position == 23 and last_position == 22:
                left = Maze.objects.get(position=24)
                right = Maze.objects.get(position=27)

                return render(request, 'maze_two_ways.html', context={
                    "right": right,
                    "left": left,
                })
            if actual_position == 23 and last_position == 24:
                left = Maze.objects.get(position=27)
                right = Maze.objects.get(position=22)

                return render(request, 'maze_two_ways.html', context={
                    "right": right,
                    "left": left,
                })
            if actual_position == 23 and last_position == 27:
                left = Maze.objects.get(position=22)
                right = Maze.objects.get(position=24)

                return render(request, 'maze_two_ways.html', context={
                    "right": right,
                    "left": left,
                })
            if actual_position == 32 and last_position == 31:
                left = Maze.objects.get(position=35)
                right = Maze.objects.get(position=33)

                return render(request, 'maze_two_ways.html', context={
                    "right": right,
                    "left": left,
                })
            if actual_position == 32 and last_position == 33:
                left = Maze.objects.get(position=31)
                right = Maze.objects.get(position=35)

                return render(request, 'maze_two_ways.html', context={
                    "right": right,
                    "left": left,
                })

        return render(request, 'maze.html', context={
            "maze": maze,
        })


class MazeIntroFightView(View):

    def get(self, request, slug):
        request.session['maze_slug'] = slug
        hero = request.session.get('actual_hero')
        hero = Hero.objects.get(id=hero)
        maze = Maze.objects.get(slug=slug)

        if maze.events == 4:
            monster = Monster.objects.filter(difficult=1)
            monster_count = monster.count()
            monster_count = randint(1, monster_count)
            monster = monster[monster_count - 1]
            messages = "Only for true heroes"
            return render(request, 'pre_fight_boss.html', context={
                'hero': hero,
                'message': messages,
                'monster': monster,
            })

        random_number = randint(1, 10)
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
        monster = Monster.objects.get(slug=slug)
        maze = request.session.get('maze_slug')
        maze = Maze.objects.get(slug=maze)

        hero = request.session.get('actual_hero')
        hero = Hero.objects.get(id=hero)

        actual_position = MazeHero.objects.get(active_position=True, hero_id=hero.id)

        last_place = Maze.objects.get(id=actual_position.position_id)
        actual_position.active_position = False
        actual_position.save()

        maze.hero.add(hero)

        new_position = MazeHero.objects.get(active_position=True, hero_id=hero.id)
        new_position.last_position = last_place.id
        new_position.save()

        user = request.user
        currency = UserCurrency.objects.get(user=user)

        if monster.difficult in [9, 10]:
            gold = monster.damage * 2
            currency.gold += monster.damage * 2

            return render(request, 'fight_chest.html', context={

            })

        fight_history = []

        while hero.health_points < 1 or monster.health_points < 1:
            hero_attack = randint(1, 6) + hero.attack_bonus
            monster_attack = randint(1, 6) + monster_attack
            monster_damage = randint(monster.dice, monster.damage) + monster.damage_bonus - hero.damage_reduction
            hero_damage = randint(hero.number_of_attacks, hero_damage) + hero.damage_bonus - monster.damage_reduction

            if hero.initiative > monster.initiative:
                if hero_attack < randint(1, 6) + monster.defence_bonus:
                    if monster_attack < randint(1, 6) + hero.defence_bonus:
                        text = "Hero attack first and miss. Monster attack second and miss."
                        fight_history.append(text)

                    text = f"Hero attack first and miss. Monster attack second and hit. " \
                           f"Hero get damage {monster_damage}."
                    fight_history.append(text)

                    if hero.health_points - monster_damage < 1:
                        text = f"{Hero.name} killed by {monster.name}"
                        fight_history.append(text)

                        hero.health_points -= monster_damage
                    hero.health_points -= monster_damage

                if monster_attack < randint(1, 6) + hero.defence_bonus:
                    text = f"Hero attack first and hit. Monster get damage {hero_damage}. " \
                           f"Monster attack second and miss."
                    fight_history.append(text)

                    if monster.health_points - hero_damage < 1:
                        text = f"{monster.name} killed by {hero.name}"
                        fight_history.append(text)

                        monster.health_points -= hero_damage
                    monster.health_points -= hero_damage

                if monster.health_points - hero_damage < 1:
                    text = f"Hero attack first and hit. Monster get damage{hero_damage}."
                    fight_history.append(text)

                    text = f"{monster.name} killed by {hero.name}"
                    fight_history.append(text)

                    monster.health_points -= hero_damage

                if hero.health_points - hero_damage < 1:
                    text = f"Hero attack first and hit. Monster get damage{hero_damage}. " \
                           f"Monster attack second and hit. Hero get damage {monster_damage}."
                    fight_history.append(text)

                    text = f"{hero.name} killed by {monster.name}."
                    fight_history.append(text)

                    hero.health_points -= monster_damage

                text = f"Hero attack first and hit. Monster get damage{hero_damage}. Monster attack second and hit. " \
                       f"Hero get damage {monster_damage}."
                fight_history.append(text)

                monster.health_points -= hero_damage
                hero.health_points -= monster_damage

            else:
                if monster_attack < randint(1, 6) + hero.defence_bonus:
                    if hero_attack < randint(1, 6) + monster.defence_bonus:
                        text = "Monster attack first and miss. Hero attack second and miss."
                        fight_history.append(text)

                    text = f"Monster attack first and miss. Hero attack second and hit. " \
                           f"Monster get damage {hero_damage}."
                    fight_history.append(text)

                    if monster.health_points - hero_damage < 1:
                        text = f"{Monster.name} killed by {hero.name}"
                        fight_history.append(text)

                        monster.health_points -= hero_damage
                    monster.health_points -= monster_damage

                if hero_attack < randint(1, 6) + monster.defence_bonus:
                    text = f"Monster attack first and hit. Hero get damage {monster_damage}. " \
                           f"Hero attack second and miss."
                    fight_history.append(text)

                    if hero.health_points - monster_damage < 1:
                        text = f"{hero.name} killed by {monster.name}"
                        fight_history.append(text)

                        hero.health_points -= monster_damage
                    hero.health_points -= monster_damage

                if hero.health_points - monster_damage < 1:
                    text = f"Monster attack first and hit. Hero get damage{monster_damage}."
                    fight_history.append(text)

                    text = f"{hero.name} killed by {monster.name}"
                    fight_history.append(text)

                    hero.health_points -= monster_damage

                if monster.health_points - hero_damage < 1:
                    text = f"Monster attack first and hit. Hero get damage{monster_damage}. " \
                           f"Hero attack second and hit. Monster get damage {hero_damage}."
                    fight_history.append(text)
                    text = f"{monster.name} killed by {hero.name}."
                    fight_history.append(text)
                    monster.health_points -= hero_damage

                text = f"Monster attack first and hit. hero get damage{monster_damage}. " \
                       f"Hero attack second and hit. Monster get damage {hero_damage}."

                fight_history.append(text)

                monster.health_points -= hero_damage
                hero.health_points -= monster_damage

        if monster.health_points < 1:
            result = "You Win!!!"
        if hero.health_points < 1:
            result = "You loose!"

        return render(request, 'fight.html', context={
            'maze': maze,
            'hero': hero,
            'result': result,
            'fight_history': fight_history,
        })
