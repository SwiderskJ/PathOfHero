from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from main.forms import LoginForm, UserCreateForm, CreateHeroForm, ArmorAddForm, WeaponAddForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from main.models import HERO_RACE
from main.models import Hero, Armor, Weapon, UserCurrency, ArmorHero, WeaponHero
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class DemoPageView(View):

    def get(self, request):
        return render(request, 'demo_page.html')


class MainView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):
        currency = UserCurrency.objects.get(user=request.user.id)
        return render(
            request,
            'main.html',
            context={
                'currency': currency
            })


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', context={
                'form': form
            }
        )

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            username = data.get('username')
            password = data.get('password')

            # authentication
            user = authenticate(
                username=username,
                password=password
            )

            if user:
                # log in
                login(request, user)
                return redirect('/hero_list/')
            else:
                return HttpResponse(f"Błąd uwierzytelnienia. Podano nieprawidłowe poświadczenia.")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(
            request,
            'logout.html'
        )


class UserCreateView(View):

    def get(self, request):
        form = UserCreateForm()
        return render(
            request,
            'create_user.html',
            context={
                'form': form,
            }
        )

    def post(self, request):
        form = UserCreateForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            user = User.objects.create_user(
                username=data.get('login'),
                password=data.get('password'),
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                email=data.get('email')
            )
            UserCurrency.objects.create(
                user=user
            )
            return redirect('/login/')


class HeroListView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):
        hero_list = Hero.objects.filter(user=request.user).order_by('is_alive', '-level')
        hero_list_count = hero_list.count()

        currency = UserCurrency.objects.get(user=request.user.id)

        return render(
            request,
            'hero_list.html',
            context={
                'hero_list': hero_list,
                'number': hero_list_count,
                'currency': currency
            })


class CreateHeroView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):
        form = CreateHeroForm()
        currency = UserCurrency.objects.get(user=request.user.id)

        return render(
            request,
            'create_hero.html',
            context={
                'form': form,
                'currency': currency,
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

            return redirect('/hero_list/')


class HeroDetailView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request, hero_id):

        hero = Hero.objects.get(id=hero_id)
        hero_race = HERO_RACE[hero.race - 1][1]
        currency = UserCurrency.objects.get(user=request.user.id)

        bought_armors = ArmorHero.objects.filter(hero_id=hero_id)
        bought_weapons = WeaponHero.objects.filter(hero_id=hero_id)

        return render(
            request,
            'hero_detail.html',
            context={
                'hero': hero,
                'hero_race': hero_race,
                'currency': currency,
                'armors': bought_armors,
                'weapons': bought_weapons,
            })

    def post(self, request, hero_id):

        request.session['actual_hero'] = hero_id

        return redirect('/main/')


class ArmoryListView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):

        hero_list = Hero.objects.filter(user=request.user).order_by('is_alive', '-level')

        if request.session.get('actual_hero') is None:
            return render(request, 'list_no_hero.html', {'hero_list': hero_list})

        armors = Armor.objects.all()
        armors_number = armors.count()

        currency = UserCurrency.objects.get(user=request.user.id)
        return render(
            request,
            'armor_list.html',
            context={
                'armors': armors,
                'armors_number': armors_number,
                'currency': currency
            })

    def post(self, request):

        hero_id = request.POST.get('hero')
        request.session['actual_hero'] = hero_id

        return redirect("/armory/")


class ArmorDetailView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request, armor_id):

        hero_list = Hero.objects.filter(user=request.user).order_by('is_alive', '-level')

        if request.session.get('actual_hero') is None:
            return render(request, 'list_no_hero.html', {'hero_list': hero_list})

        armor = Armor.objects.get(id=armor_id)
        currency = UserCurrency.objects.get(user=request.user.id)

        return render(
            request,
            'armor_detail.html',
            context={
                'armor': armor,
                'currency': currency
            })

    def post(self, request, armor_id):

        hero_id = request.POST.get('hero')
        request.session['actual_hero'] = hero_id

        return redirect(f"/armor_details/{armor_id}/")


class AddArmorView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):

        form = ArmorAddForm()
        currency = UserCurrency.objects.get(user=request.user.id)

        return render(
            request,
            'add_armor.html',
            context={
                'form': form,
                'currency': currency
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

            return redirect('/armory/')


class SmithListView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):

        hero_list = Hero.objects.filter(user=request.user).order_by('is_alive', '-level')

        if request.session.get('actual_hero') is None:
            currency = UserCurrency.objects.get(user=request.user.id)

            return render(
                request,
                'list_no_hero.html',
                context={
                    'hero_list': hero_list,
                    'currency': currency,
                })

        weapons = Weapon.objects.all().order_by('price', 'attack_bonus')
        weapons_number = weapons.count()
        currency = UserCurrency.objects.get(user=request.user.id)

        return render(
            request,
            'smith_list.html',
            context={
                'weapons': weapons,
                'weapons_number': weapons_number,
                'currency': currency
            })

    def post(self, request):

        hero_id = request.POST.get('hero')
        request.session['actual_hero'] = hero_id

        return redirect("/smith/")


class WeaponDetailView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request, weapon_id):
        hero_list = Hero.objects.filter(user=request.user).order_by('is_alive', '-level')

        if request.session.get('actual_hero') is None:
            currency = UserCurrency.objects.get(user=request.user.id)

            return render(
                request,
                'list_no_hero.html',
                context={
                    'hero_list': hero_list,
                    'currency': currency,
                })

        weapon = Weapon.objects.get(id=weapon_id)
        currency = UserCurrency.objects.get(user=request.user.id)

        return render(request, 'weapon_detail.html', {
            'weapon': weapon,
            'currency': currency
        })

    def post(self, request, weapon_id):
        hero_id = request.POST.get('hero')
        request.session['actual_hero'] = hero_id

        return redirect(f"/weapon_details/{weapon_id}/")


class AddWeaponView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):
        currency = UserCurrency.objects.get(user=request.user.id)
        form = WeaponAddForm()

        return render(
            request,
            'add_weapon.html',
            context={
                'form': form,
                'currency': currency
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

            return redirect('/smith/')


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
                'currency': currency,
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

        return redirect('/smith/')


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

        return redirect('/armory/')

