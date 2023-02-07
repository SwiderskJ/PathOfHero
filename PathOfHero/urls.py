from django.contrib import admin
from django.urls import path
from hero_app.views import HeroListView, CreateHeroView, BuyArmorView, ArmorDetailView, BuyWeaponView, \
     ArmoryListView, SmithListView, AddArmorView, AddWeaponView, WeaponDetailView, HeroDetailView
from user_app.views import DemoPageView, LoginView, LogoutView, MainView, UserCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DemoPageView.as_view(), name='demo_page'),
    path('main/', MainView.as_view(), name='main_site'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('hero_list/', HeroListView.as_view(), name='hero_list'),
    path('hero_details/<int:hero_id>/', HeroDetailView.as_view(), name='hero_detail'),
    path('create_hero/', CreateHeroView.as_view(), name='create_hero'),
    path('armory/', ArmoryListView.as_view(), name='armory'),
    path('armor_details/<int:armor_id>/', ArmorDetailView.as_view(), name='armor_detail'),
    path('buy_armor/<int:armor_id>/', BuyArmorView.as_view(), name='buy_armor'),
    path('add_armor/', AddArmorView.as_view(), name='add_armor'),
    path('smith/', SmithListView.as_view(), name='smith'),
    path('weapon_details/<int:weapon_id>/', WeaponDetailView.as_view(), name='weapon_details'),
    path('buy_weapon/<int:weapon_id>/', BuyWeaponView.as_view(), name='buy_weapon'),
    path('add_weapon/', AddWeaponView.as_view(), name='add_weapon'),
]
