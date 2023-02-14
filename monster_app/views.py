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
        user = request.user
        if user.is_staff:
            form = MonsterForm()

            return render(request, 'new_monster.html', {'form': form})

        else:
            return redirect(reverse('main_site'))

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
