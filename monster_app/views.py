from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse_lazy, reverse
from monster_app.forms import MonsterForm
from monster_app.models import Monster


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



