from random import randint
from django.shortcuts import render, redirect
from django.views import View

from gameplay_app.functions import dice
from gameplay_app.models import MazeHero, Maze
from hero_app.models import Hero
from monster_app.models import Monster
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from user_app.models import UserCurrency


class EntryMazeView(LoginRequiredMixin, View):  # First view when user enter first time to maze.
    login_url = reverse_lazy('login')

    def get(self, request):
        # The method starts by checking if the actual_hero is stored in the session.
        if request.session.get('actual_hero') is None:
            # If the actual_hero is not found in the session, the user is redirected to the hero_list view.
            return redirect(reverse('hero_list'))

        # The hero object is retrieved from the database using the Hero model and the id stored in the session.
        hero = request.session.get('actual_hero')
        hero = Hero.objects.get(id=hero)

        # Actual position of the hero in the maze is determined by querying the MazeHero model for the hero.
        actual_position = MazeHero.objects.get(hero_id=hero.id, active_position=True)
        actual_position = Maze.objects.get(position=actual_position.position.position)

        # If the position of the actual position of the hero is greater than 1, the user is redirected to the maze view.
        if actual_position.position > 1:
            return redirect(reverse('maze'))

        # If the position is 1, the render function is called to render the maze_entry.html
        return render(request, 'maze_entry.html', context={
            'hero': hero,
            'maze': actual_position,
        })


class MazeMovementView(LoginRequiredMixin, View):  # Simulate moving on Maze.
    login_url = reverse_lazy('login')

    def get(self, request):
        # The method starts by checking if the actual_hero is stored in the session.
        if request.session.get('actual_hero') is None:
            # If the actual_hero is not found in the session, the user is redirected to the hero_list view.
            return redirect(reverse('hero_list'))

        # # The hero object is retrieved from the database using the Hero model and the id stored in the session.
        hero = request.session.get('actual_hero')
        hero = Hero.objects.get(id=hero)

        # Actual position of the hero in the maze is determined by querying the MazeHero model for the hero.
        actual_position = MazeHero.objects.filter(active_position=True, hero_id=hero.id)

        last_position = actual_position[0].last_position

        actual_position = actual_position[0].position.position

        # Retrieves the hero's next position in the maze from the MazeHero model.
        maze = Maze.objects.get(position=actual_position)

        # The code then checks the events field of the maze object to determine what should be displayed to the user.
        if maze.events == 3:
            # If events is equal to 3, the maze_endpoint.html template will be rendered.
            maze = Maze.objects.get(position=last_position)
            return render(request, 'maze_endpoint.html', context={
                'maze': maze
            })

        if maze.events == 4:
            # If events is equal to 4, the boss.html template will be rendered.
            maze = Maze.objects.get(position=1)
            return render(request, 'boss.html', context={
                'maze': maze,
            })

        if maze.events == 2:
            # If events is equal to 2, the code retrieves the maze objects.
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
        if maze.events == 1:
            if actual_position == 13 and last_position == 12:
                maze = Maze.objects.get(position=6)

            elif actual_position == 14 and last_position == 15:
                maze = Maze.objects.get(position=4)
            elif actual_position == 27 and last_position == 28:
                maze = Maze.objects.get(position=23)
            elif actual_position == 1 and last_position == 2:
                maze = Maze.objects.get(position=2)
                return render(request, 'maze_out.html', context={
                    'maze': maze,
                })

            else:
                if actual_position > last_position:
                    maze = Maze.objects.get(position=actual_position + 1)
                if actual_position < last_position:
                    maze = Maze.objects.get(position=actual_position - 1)
                if actual_position == last_position:
                    maze = Maze.objects.get(position=actual_position + 1)

        print(maze)
        # If events is not in [2, 3, 4], the maze.html template will be rendered.
        return render(request, 'maze.html', context={
            "maze": maze,
        })


class MazeIntroFightView(LoginRequiredMixin, View):  # Class-based view for handling a pre-fight view.
    login_url = reverse_lazy('login')

    def get(self, request, slug):
        # The method starts by checking if the actual_hero is stored in the session.
        if request.session.get('actual_hero') is None:
            # If the actual_hero is not found in the session, the user is redirected to the hero_list view.
            return redirect(reverse('hero_list'))

        request.session['maze_slug'] = slug
        hero = request.session.get('actual_hero')
        hero = Hero.objects.get(id=hero)
        maze = Maze.objects.get(slug=slug)


        if maze.position == 38:
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

        if maze.position < 10:
            random_number = randint(6, 10)
        elif 9 < maze.position < 18:
            random_number = randint(5, 9)
        elif 17 < maze.position < 25:
            random_number = randint(4, 8)
        elif 24 < maze.position < 31:
            random_number = randint(3, 7)
        else:
            random_number = randint(2, 3)

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


class FightView(LoginRequiredMixin, View):  # Class-based view for handling a fight between a hero and a monster.
    login_url = reverse_lazy('login')

    def get(self, request, slug):
        # The method starts by checking if the actual_hero is stored in the session.
        if request.session.get('actual_hero') is None:
            # If the actual_hero is not found in the session, the user is redirected to the hero_list view.
            return redirect(reverse('hero_list'))

        monster = Monster.objects.get(slug=slug)

        maze = request.session.get('maze_slug')
        next_position = Maze.objects.get(slug=maze)

        hero = request.session.get('actual_hero')
        hero = Hero.objects.get(id=hero)

        actual_position = MazeHero.objects.get(active_position=True, hero_id=hero.id)

        next_maze_hero = MazeHero.objects.filter(hero_id=hero.id, position_id=next_position.id)
        user = request.user
        currency = UserCurrency.objects.get(user=user)
        begin_currency = currency.gold

        if monster.difficult in [9, 10]:
            currency.gold += monster.prize
            currency.save()

            last_place = Maze.objects.get(id=actual_position.position_id).position
            actual_position.active_position = False
            actual_position.save()

            if next_maze_hero:
                next_maze_hero[0].active_position = True
                next_maze_hero[0].last_position = last_place
                next_maze_hero[0].save()
            else:
                next_position.hero.add(hero)

                new_position = MazeHero.objects.get(active_position=True, hero_id=hero.id)
                new_position.last_position = last_place
                new_position.save()

            return render(request, 'fight_chest.html', context={
                'chest': monster,
                'currency': currency,
                'begin_currency': begin_currency,
            })

        fight_history = []
        monster_health = monster.health_points
        hero_health = hero.health_points
        while hero_health > 0 or monster_health > 0:
            if hero_health < 1:
                break
            if monster_health< 1:
                break

            monster_damage = 0
            item = 0
            while item == monster.number_of_attacks:
                monster_damage += dice(monster.damage) + monster.damage_bonus
                item += 1

            hero_damage = 0
            item = 0
            while item == hero.number_of_attacks:
                hero_damage += dice(hero.damage) + hero.damage_bonus
                item += 1
                print(hero_damage)
            print(hero_damage)

            hero_attack = dice(20) + hero.attack_bonus
            monster_attack = dice(20) + monster.attack_bonus
            hero_defence = dice(20) + hero.defence_bonus
            monster_defence = dice(20) + monster.defence_bonus
            hero_initiative = dice(20) + hero.initiative
            monster_initiative = dice(20) + monster.initiative

            if hero_initiative >= monster_initiative:

                # Hero starts and miss.
                if hero_attack <= monster_defence:
                    if monster_attack <= hero_defence:
                        text = "Hero attack first and miss. Monster attack second and miss."
                        fight_history.append(text)

                    text = f"Hero attack first and miss. Monster attack second and hit. " \
                           f"Hero get damage {monster_damage}."
                    fight_history.append(text)

                    if hero.health_points - monster_damage < 1:
                        text = f"{Hero.name} killed by {monster.name}"
                        fight_history.append(text)

                        hero_health -= monster_damage
                        break
                    else:
                        hero_health -= monster_damage

                # Hero starts and hit.
                if hero_attack > monster_defence:

                    if monster_attack <= hero_defence:
                        text = f"Hero attack first and hit. Monster get damage {hero_damage}."
                        fight_history.append(text)

                        if monster.health_points - hero_damage < 1:
                            text = f"{monster.name} killed by {hero.name}"
                            fight_history.append(text)

                            monster_health -= hero_damage
                            break
                        else:
                            text = "Monster attack second and miss."
                            fight_history.append(text)
                            monster_health -= hero_damage

                    if monster_attack > hero_defence:
                        text = f"Hero attack first and hit. Monster get damage {hero_damage}"
                        fight_history.append(text)

                        if monster.health_points - hero_damage < 1:
                            text = f"{monster.name} killed by {hero.name}"
                            fight_history.append(text)

                            monster_health -= hero_damage
                            break
                        else:
                            monster_health -= hero_damage

                        text = f"Monster attack second and hit. Hero get damage {monster_damage}"
                        fight_history.append(text)

                        if hero.health_points - monster_damage < 1:
                            text = f"{hero.name} killed by {monster.name}"
                            fight_history.append(text)

                            hero_health -= monster_damage
                            break
                        else:
                            hero_health -= monster_damage

            else:
                # Monster starts and miss.
                if monster_attack <= hero_defence:
                    if hero_attack <= monster_defence:
                        text = "Monster attack first and miss. Hero attack second and miss."
                        fight_history.append(text)
                    else:
                        text = f"Monster attack first and miss. Hero attack second and hit. " \
                           f"Monster get damage {hero_damage}."
                        fight_history.append(text)

                        if monster.health_points - hero_damage < 1:
                            text = f"{monster.name} killed by {hero.name}"
                            fight_history.append(text)

                            monster_health -= hero_damage
                            break
                        else:
                            monster_health -= hero_damage

                # Monster starts and hit.
                if monster_attack >= hero_defence:

                    if hero_attack <= monster_defence:
                        text = f"Monster attack first and hit. Hero get damage {monster_damage}."
                        fight_history.append(text)

                        if hero.health_points - monster_damage < 1:
                            text = f"{hero.name} killed by {monster.name}"
                            fight_history.append(text)

                            hero_health -= monster_damage
                            break
                        else:
                            text = "Hero attack second and miss."
                            fight_history.append(text)
                            hero_health -= monster_damage

                    else:
                        text = f"Monster attack first and hit. Hero get damage {monster_damage}"
                        fight_history.append(text)

                        if hero.health_points - monster_damage < 1:
                            text = f"{hero.name} killed by {monster.name}"
                            fight_history.append(text)

                            hero_health -= monster_damage
                            break
                        else:
                            text = f"Hero attack second and hit. Monster get damage {hero_damage}"
                            fight_history.append(text)

                            if monster.health_points - hero_damage < 1:
                                text = f"{monster.name} killed by {hero.name}"
                                fight_history.append(text)

                                monster_health -= hero_damage
                                break
                            else:
                                monster_health -= hero_damage

        hero.health_points = hero_health
        hero.save()

        if hero.health_points < 1:
            result = "You loose!"
            return render(request, 'fight_loose.html', context={
                'maze': maze,
                'hero': hero,
                'result': result,
                'fight_history': fight_history,
                'monster': monster,
                'monster_health': monster_health,
            })

        currency.gold += monster.prize
        currency.save()

        last_place = Maze.objects.get(id=actual_position.position_id).position
        actual_position.active_position = False
        actual_position.save()
        result = "You Win!!!"

        if next_position.position == 1 and last_place > 2:
            next_maze = MazeHero.objects.get(position=Maze.objects.get(position=1).id, hero_id=hero.id)
            next_maze.active_position = True
            next_maze.last_position = 1
            next_maze.save()

            return render(request, 'beat_maze.html', context={
                'maze': maze,
                'hero': hero,
                'result': result,
                'fight_history': fight_history,
                'monster': monster,
                'monster_health': monster_health
            })

        if next_maze_hero:
            next_maze_hero[0].active_position = True
            next_maze_hero[0].last_position = last_place
            next_maze_hero[0].save()

        else:
            next_position.hero.add(hero)

            new_position = MazeHero.objects.get(active_position=True, hero_id=hero.id)
            new_position.last_position = last_place
            new_position.save()

        return render(request, 'fight.html', context={
            'maze': maze,
            'hero': hero,
            'result': result,
            'fight_history': fight_history,
            'monster': monster,
            'monster_health': monster_health
        })

    def post(self, request, slug):
        monster = Monster.objects.get(slug=slug)
        monster.health_points = monster.max_health_points
        monster.save()
        hero = request.session.get('actual_hero')
        hero = Hero.objects.get(id=hero)
        return render(request, 'after_battle.html', context={
            'hero': hero,
        })
