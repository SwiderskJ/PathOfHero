from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse_lazy, reverse
from monster_app.forms import MonsterForm
from monster_app.models import Monster


class MonsterList(LoginRequiredMixin, View):  # Used to display a list of all the monsters stored in the database,
    login_url = reverse_lazy('login')

    def get(self, request):
        monsters = Monster.objects.all().order_by('difficult', 'damage_reduction')
        return render(request, 'monster_list.html', {'monsters': monsters})


class CreateMonsterView(LoginRequiredMixin, View):  # This view is used to create a new monster in the database.
    login_url = reverse_lazy('login')

    def get(self, request):
        form = MonsterForm()

        return render(request, 'new_monster.html', {'form': form})

    def post(self, request):
        form = MonsterForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            Monster.objects.create(
                name=data.get('name'),
                strength=data.get('strength'),
                dexterity=data.get('dexterity'),
                endurance=data.get('endurance'),
                intelligence=data.get('intelligence'),
                wisdom=data.get('wisdom'),
                charisma=data.get('charisma'),
                max_health_points=data.get('max_health_points'),
                damage_reduction=data.get('damage_reduction'),
                number_of_attacks=data.get('number_of_attacks'),
                damage=data.get('damage'),
                initiative=data.get('initiative'),
                defence_bonus=data.get('defence_bonus'),
                difficult=data.get('difficult'),
                experience=data.get('experience'),

            )

            return redirect(reverse('create_monster'))


# class EditMonsterView(LoginRequiredMixin, View):  # This view is used to edit an existing monster in the database.
#     login_url = reverse_lazy('login')
#
#     def get(self, request, slug):
#         monster = Monster.objects.get(slug=slug)
#         form = MonsterForm(initial={
#             'name': monster.name,
#             'level': monster.level,
#             'strength': monster.strength,
#             'dexterity': monster.dexterity,
#             'endurance': monster.wisdom,
#             'intelligence': monster.endurance,
#             'wisdom': monster.difficult,
#             'charisma': monster.damage_reduction,
#             'difficult': monster.number_of_dices,
#             'damage_reduction': monster.dice,
#             'number_of_attacks': monster.number_of_attacks,
#             'damage': monster.damage,
#             'experience': monster.experience,
#             })
#
#         return render(request, 'edit_monster.html', {'form': form, 'monster': monster})
#
#     def post(self, request, monster_id):
#         form = MonsterForm(request.POST)
#
#         if form.is_valid():
#             data = form.cleaned_data
#             monster = Monster.objects.get(id=monster_id)
#
#             monster.name = data.get('name')
#             monster.level = data.get('level')
#             monster.strength = data.get('strength')
#             monster.dexterity = data.get('dexterity')
#             monster.wisdom = data.get('wisdom')
#             monster.endurance = data.get('endurance')
#             monster.max_health_points = monster.endurance * 4
#             monster.health_points = monster.max_health_points
#             monster.difficult = data.get('difficult')
#             monster.damage_reduction = data.get('damage_reduction')
#             monster.number_of_dices = data.get('number_of_dices')
#             monster.dice = data.get('dice')
#             monster.damage_bonus = monster.strength
#             monster.attack_bonus = monster.dexterity
#             monster.defence_bonus = monster.wisdom
#             monster.initiative = monster.wisdom + monster.dexterity
#             monster_dice = int(monster.dice)
#             monster_dice = DICE[monster_dice - 1]
#             monster_dice = monster_dice[1]
#             monster.damage = monster_dice * monster.number_of_dices
#             monster.save()
#
#             return redirect(reverse('monster_list'))
