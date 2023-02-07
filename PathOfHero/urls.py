"""PathOfHero URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from PathOfHero import settings
from main.views import DemoPageView, LoginView, UserCreateView, LogoutView, MainView, HeroListView, CreateHeroView, \
    BuyWeaponView, HeroDetailView, ArmoryListView, SmithListView, AddArmorView, AddWeaponView, WeaponDetailView, \
    BuyArmorView
from main.views import ArmorDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DemoPageView.as_view()),
    path('main/', MainView.as_view()),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view()),
    path('register/', UserCreateView.as_view()),
    path('hero_list/', HeroListView.as_view()),
    path('hero_details/<int:hero_id>/', HeroDetailView.as_view()),
    path('create_hero/', CreateHeroView.as_view()),
    path('armory/', ArmoryListView.as_view()),
    path('armor_details/<int:armor_id>/', ArmorDetailView.as_view()),
    path('buy_armor/<int:armor_id>/', BuyArmorView.as_view()),
    path('add_armor/', AddArmorView.as_view()),
    path('smith/', SmithListView.as_view()),
    path('weapon_details/<int:weapon_id>/', WeaponDetailView.as_view()),
    path('buy_weapon/<int:weapon_id>/', BuyWeaponView.as_view()),
    path('add_weapon/', AddWeaponView.as_view()),
]
