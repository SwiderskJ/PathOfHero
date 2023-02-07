
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from main.forms import LoginForm, UserCreateForm, CreateHeroForm, ArmorAddForm, WeaponAddForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from main.models import HERO_RACE
from main.models import Hero, Armor, Weapon
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class DemoPageView(View):

    def get(self, request):
        return render(request, 'demo_page.html')


class MainView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):
        return render(request, 'main.html')


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(
            request,
            'login.html',
            context={
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

            User.objects.create_user(
                username=data.get('login'),
                password=data.get('password'),
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                email=data.get('email')
            )
            return redirect('/login/')


class HeroListView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):
        hero_list = Hero.objects.filter(user=request.user).order_by('is_alive', '-level')
        hero_list_count = hero_list.count()
        return render(request, 'hero_list.html', {'hero_list': hero_list, 'number': hero_list_count})


class CreateHeroView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):
        form = CreateHeroForm()
        return render(request, 'create_hero.html', {'form': form})

    def post(self, request):
        form = CreateHeroForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            max_health_points = data.get('endurance')*4
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
        hero_race = HERO_RACE[hero.race-1][1]
        return render(request, 'hero_detail.html', {'hero': hero, 'hero_race': hero_race})

    def post(self, request, hero_id):
        request.session['actual_hero'] = hero_id
        return redirect('/main/')


class ArmoryListView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):
        hero_list = Hero.objects.filter(user=request.user).order_by('is_alive', '-level')
        if request.session.get('actual_hero') is None:
            return render(request, 'list_no_hero.html', {'hero_list': hero_list})
        armors = Armor.objects.all().order_by('price', 'defence_bonus')
        armors_number = armors.count()
        return render(request, 'armor_list.html', {'armors': armors, 'armors_number': armors_number})

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
        return render(request, 'armor_detail.html', {'armor': armor})

    def post(self, request, armor_id):
        hero_id = request.POST.get('hero')
        request.session['actual_hero'] = hero_id
        return redirect(f"/armor_details/{armor_id}/")



class AddArmorView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):
        form = ArmorAddForm()
        return render(request, 'add_armor.html', {'form': form})

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
                price=data.get('price')
            )

            return redirect('/armory/')


class SmithListView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):
        hero_list = Hero.objects.filter(user=request.user).order_by('is_alive', '-level')
        if request.session.get('actual_hero') is None:
            return render(request, 'list_no_hero.html', {'hero_list': hero_list})
        weapons = Weapon.objects.all().order_by('price', 'attack_bonus')
        weapons_number = weapons.count()
        return render(request, 'smith_list.html', {'weapons': weapons, 'weapons_number': weapons_number})

    def post(self, request):
        hero_id = request.POST.get('hero')
        request.session['actual_hero'] = hero_id
        return redirect("/smith/")


class WeaponDetailView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request, weapon_id):
        hero_list = Hero.objects.filter(user=request.user).order_by('is_alive', '-level')
        if request.session.get('actual_hero') is None:
            return render(request, 'list_no_hero.html', {'hero_list': hero_list})
        weapon = Weapon.objects.get(id=weapon_id)
        return render(request, 'weapon_detail.html', {'weapon': weapon})

    def post(self, request, weapon_id):
        hero_id = request.POST.get('hero')
        request.session['actual_hero'] = hero_id
        return redirect(f"/weapon_details/{weapon_id}/")


class AddWeaponView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):
        form = WeaponAddForm()
        return render(request, 'add_weapon.html', {'form': form})

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
                price=data.get('price')
            )

            return redirect('/smith/')
