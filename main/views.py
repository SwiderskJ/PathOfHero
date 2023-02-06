
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse
from main.forms import LoginForm, UserCreateForm, CreateHeroForm, ArmorAddForm, WeaponAddForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from main.models import HERO_RACE
from main.models import Hero, Armor, Weapon
# Create your views here.


class DemoPageView(View):

    def get(self, request):
        return render(request, 'demopage.html')


class MainView(View):

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

            # uwierzytelnienie
            user = authenticate(
                username=username,
                password=password
            )

            if user:
                # logowanie
                login(request, user)
                return redirect('/main/')
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


class HeroListView(View):

    def get(self, request):
        hero_list = Hero.objects.filter(user=request.user).order_by('is_alive', '-level')
        hero_list_count = hero_list.count()
        return render(request, 'hero_list.html', {'hero_list': hero_list, 'number': hero_list_count})


class CreateHeroView(View):

    def get(self, request):
        form = CreateHeroForm()
        return render(request, 'create_hero.html', {'form': form})

    def post(self, request):
        form = CreateHeroForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            max_health_points = data.get('endurance')*4
            health_points = max_health_points
            Hero.objects.create(
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

            return redirect('/hero_list/')


class HeroDetailView(View):

    def get(self, request, hero_id):
        hero = Hero.objects.get(id=hero_id)
        hero_race = HERO_RACE[hero.race-1][1]
        return render(request, 'hero_detail.html', {'hero': hero, 'hero_race': hero_race})


class ArmoryListView(View):

    def get(self, request):
        armors = Armor.objects.all().order_by('price', 'defence_bonus')
        armors_number = armors.count()
        return render(request, 'armor_list.html', {'armors': armors, 'armors_number': armors_number})


class AddArmorView(View):

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


class AddWeaponView(View):

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