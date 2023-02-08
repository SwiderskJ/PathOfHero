from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse_lazy, reverse
from monster_app.forms import MonsterForm
from monster_app.models import Monster


class MonsterList(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):
        monsters = Monster.objects.all().order_by('difficult', 'damage_reduction')
        return render(request, 'monster_list.html', {'monsters': monsters})


class CreateMonsterView(LoginRequiredMixin, View):
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
                level=data.get('level'),
                strength=data.get('strength'),
                dexterity=data.get('dexterity'),
                wisdom=data.get('wisdom'),
                endurance=data.get('endurance'),
                health_points=data.get('max_health_points'),
                max_health_points=data.get('max_health_points'),
                difficult=data.get('difficult'),
                damage_reduction=data.get('damage_reduction'),
                number_of_dices=data.get('number_of_dices'),
                dice=data.get('dice'),
            )

            return redirect(reverse('create_monster'))


class EditMonsterView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request, monster_id):
        monster = Monster.objects.get(id=monster_id)
        form = MonsterForm(initial={
            'name': monster.name,
            'level': monster.level,
            'strength': monster.strength,
            'dexterity': monster.dexterity,
            'wisdom': monster.wisdom,
            'endurance': monster.endurance,
            'max_health_points': monster.max_health_points,
            'difficult': monster.difficult,
            'damage_reduction': monster.damage_reduction,
            'number_of_dices': monster.number_of_dices,
            'dice': monster.dice
            })

        return render(request, 'edit_monster.html', {'form': form, 'monster': monster})

    def post(self, request, monster_id):
        form = MonsterForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            monster = Monster.objects.get(id=monster_id)

            monster.name = data.get('name')
            monster.level = data.get('level')
            monster.strength = data.get('strength')
            monster.dexterity = data.get('dexterity')
            monster.wisdom = data.get('wisdom')
            monster.endurance = data.get('endurance')
            monster.health_points = data.get('max_health_points')
            monster.max_health_points = data.get('max_health_points')
            monster.difficult = data.get('difficult')
            monster.damage_reduction = data.get('damage_reduction')
            monster.number_of_dices = data.get('number_of_dices')
            monster.dice = data.get('dice')
            monster.save()

            return redirect(reverse('monster_list'))
