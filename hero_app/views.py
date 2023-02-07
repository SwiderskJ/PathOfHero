from audioop import reverse

from django.shortcuts import render, redirect
from django.views import View
from hero_app.forms import CreateHeroForm, ArmorAddForm, WeaponAddForm
from hero_app.models import HERO_RACE
from hero_app.models import Hero, Armor, Weapon, ArmorHero, WeaponHero
from user_app.models import UserCurrency
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class HeroListView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):
        hero_list = Hero.objects.filter(user=request.user).order_by('is_alive', '-level')
        hero_list_count = hero_list.count()

        return render(
            request,
            'hero_list.html',
            context={
                'hero_list': hero_list,
                'number': hero_list_count,
            })


class CreateHeroView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):
        form = CreateHeroForm()

        return render(
            request,
            'create_hero.html',
            context={
                'form': form,
            })

    def post(self, request):
        form = CreateHeroForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            max_health_points = data.get('endurance') * 4
            health_points = max_health_points

            hero = Hero.objects.create(
                name=data.get('name'),
                race=data.get('race'),
                strength=data.get('strength'),
                dexterity=data.get('dexterity'),
                wisdom=data.get('wisdom'),
                endurance=data.get('endurance'),
                max_health_points=max_health_points,
                health_points=health_points,
                user=request.user
            )

            request.session['actual_hero'] = hero.id

            return redirect(reverse('hero_list'))


class HeroDetailView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request, hero_id):

        hero = Hero.objects.get(id=hero_id)
        hero_race = HERO_RACE[hero.race - 1][1]

        bought_armors = ArmorHero.objects.filter(hero_id=hero_id)
        bought_weapons = WeaponHero.objects.filter(hero_id=hero_id)

        return render(
            request,
            'hero_detail.html',
            context={
                'hero': hero,
                'hero_race': hero_race,
                'armors': bought_armors,
                'weapons': bought_weapons,
            })

    def post(self, request, hero_id):

        request.session['actual_hero'] = hero_id

        return redirect(reverse('main_site'))


class ArmoryListView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):

        hero_list = Hero.objects.filter(user=request.user).order_by('is_alive', '-level')

        if request.session.get('actual_hero') is None:
            return render(request, 'list_no_hero.html', {'hero_list': hero_list})

        armors = Armor.objects.all()
        armors_number = armors.count()

        return render(
            request,
            'armor_list.html',
            context={
                'armors': armors,
                'armors_number': armors_number,
            })

    def post(self, request):

        hero_id = request.POST.get('hero')
        request.session['actual_hero'] = hero_id

        return redirect(reverse('armory'))


class ArmorDetailView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request, armor_id):

        hero_list = Hero.objects.filter(user=request.user).order_by('is_alive', '-level')

        if request.session.get('actual_hero') is None:
            return render(request, 'list_no_hero.html', {'hero_list': hero_list})

        armor = Armor.objects.get(id=armor_id)

        return render(
            request,
            'armor_detail.html',
            context={
                'armor': armor,
            })

    def post(self, request, armor_id):

        hero_id = request.POST.get('hero')
        request.session['actual_hero'] = hero_id

        return redirect(reverse('armor_detail',armor_id))


class AddArmorView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):

        form = ArmorAddForm()

        return render(
            request,
            'add_armor.html',
            context={
                'form': form,
            })

    def post(self, request):

        form = ArmorAddForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            Armor.objects.create(
                name=data.get('name'),
                description=data.get('description'),
                defence_bonus=data.get('defence_bonus'),
                attack_bonus=data.get('attack_bonus'),
                damage_reduction=data.get('damage_reduction'),
                price=data.get('price'),
                diamonds=data.get('diamonds')
            )

            return redirect(reverse('armory'))


class SmithListView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):

        hero_list = Hero.objects.filter(user=request.user).order_by('is_alive', '-level')

        if request.session.get('actual_hero') is None:

            return render(
                request,
                'list_no_hero.html',
                context={
                    'hero_list': hero_list,
                })

        weapons = Weapon.objects.all().order_by('price', 'attack_bonus')
        weapons_number = weapons.count()

        return render(
            request,
            'smith_list.html',
            context={
                'weapons': weapons,
                'weapons_number': weapons_number,
            })

    def post(self, request):

        hero_id = request.POST.get('hero')
        request.session['actual_hero'] = hero_id

        return redirect(reverse('smith'))


class WeaponDetailView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request, weapon_id):
        hero_list = Hero.objects.filter(user=request.user).order_by('is_alive', '-level')

        if request.session.get('actual_hero') is None:

            return render(
                request,
                'list_no_hero.html',
                context={
                    'hero_list': hero_list,
                })

        weapon = Weapon.objects.get(id=weapon_id)

        return render(request, 'weapon_detail.html', {
            'weapon': weapon,
        })

    def post(self, request, weapon_id):
        hero_id = request.POST.get('hero')
        request.session['actual_hero'] = hero_id

        return redirect(reverse('weapon_details',weapon_id))


class AddWeaponView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):
        form = WeaponAddForm()

        return render(
            request,
            'add_weapon.html',
            context={
                'form': form,
            })

    def post(self, request):
        form = WeaponAddForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            Weapon.objects.create(
                name=data.get('name'),
                description=data.get('description'),
                defence_bonus=data.get('defence_bonus'),
                attack_bonus=data.get('attack_bonus'),
                damage_bonus=data.get('damage_bonus'),
                price=data.get('price'),
                diamonds=data.get('diamonds')
            )

            return redirect(reverse('smith'))


class BuyWeaponView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request, weapon_id):
        currency = UserCurrency.objects.get(user=request.user.id)
        weapon = Weapon.objects.get(id=weapon_id)

        gold_balance = currency.gold - weapon.price
        diamonds_balance = currency.diamonds - weapon.diamonds

        return render(
            request,
            'buy_weapon.html',
            context={
                'weapon': weapon,
                'gold_balance': gold_balance,
                'diamond_balance': diamonds_balance
            })

    def post(self, request, weapon_id):
        hero = Hero.objects.get(id=request.session.get('actual_hero'))
        currency = UserCurrency.objects.get(user=request.user.id)
        weapon = Weapon.objects.get(id=weapon_id)

        gold_balance = currency.gold - weapon.price
        diamonds_balance = currency.diamonds - weapon.diamonds

        currency.gold = gold_balance
        currency.diamonds = diamonds_balance
        currency.save()

        weapon.hero.add(hero)

        return redirect(reverse('smith'))


class BuyArmorView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request, armor_id):
        currency = UserCurrency.objects.get(user=request.user.id)
        armor = Armor.objects.get(id=armor_id)

        gold_balance = currency.gold - armor.price
        diamonds_balance = currency.diamonds - armor.diamonds

        return render(
            request,
            'buy_armor.html',
            context={
                'currency': currency,
                'armor': armor,
                'gold_balance': gold_balance,
                'diamond_balance': diamonds_balance
            })

    def post(self, request, armor_id):
        hero = Hero.objects.get(id=request.session.get('actual_hero'))
        currency = UserCurrency.objects.get(user=request.user.id)
        armor = Armor.objects.get(id=armor_id)

        gold_balance = currency.gold - armor.price
        diamonds_balance = currency.diamonds - armor.diamonds

        currency.gold = gold_balance
        currency.diamonds = diamonds_balance
        currency.save()

        armor.hero.add(hero)

        return redirect(reverse('armory'))
