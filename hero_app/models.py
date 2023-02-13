
from django.db import models
from django.contrib.auth.models import User
from random import randint

HERO_RACE = (
    (1, "Human"),
    (2, "Dwarf"),
    (3, "Elf"),
    (4, "Gnome"),
    (5, "Half-elf"),
    (6, "Half-orc"),
    (7, "Halfling")
)

WEAPON = (
    (1, "Attack without weapon"),
    (2, "Light melee weapon"),
    (3, "One-handed combat weapon"),
    (4, "A two-handed melee weapon"),

)

WEAPON_CLASS = (
    (1, "Simple Weapons"),
    (2, "Soldier's weapon"),
    (3, "Exotic weapons"),
)
ARMOR = (
    (1, "Light Armor"),
    (2, "Medium Armor"),
    (3, "Heavy armor")
)


class Hero(models.Model):
    name = models.CharField(max_length=16)
    race = models.IntegerField(choices=HERO_RACE)
    experience_points = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    strength = models.IntegerField(default=0)
    dexterity = models.IntegerField(default=0)
    endurance = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)
    wisdom = models.IntegerField(default=0)
    charisma = models.IntegerField(default=0)
    health_points = models.IntegerField(default=0)
    max_health_points = models.IntegerField(default=0)
    is_alive = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attack_bonus = models.IntegerField(default=0)
    defence_bonus = models.IntegerField(default=0)
    damage_reduction = models.IntegerField(default=0)
    damage_bonus = models.IntegerField(default=0)
    damage = models.IntegerField(default=2)
    initiative = models.IntegerField(default=0)
    number_of_attacks = models.IntegerField(default=1)
    strength_bonus = models.IntegerField(default=0)
    dexterity_bonus = models.IntegerField(default=0)
    endurance_bonus = models.IntegerField(default=0)
    intelligence_bonus = models.IntegerField(default=0)
    wisdom_bonus = models.IntegerField(default=0)
    charisma_bonus = models.IntegerField(default=0)


class Armor(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    defence_bonus = models.IntegerField()
    damage_reduction = models.IntegerField()
    price = models.IntegerField(default=0)
    diamonds = models.IntegerField(default=0)
    hero = models.ManyToManyField(Hero, through='ArmorHero')
    type = models.IntegerField(choices=ARMOR, default=1)


class Weapon(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    attack_bonus = models.IntegerField()
    damage_bonus = models.IntegerField()
    price = models.IntegerField(default=0)
    diamonds = models.IntegerField(default=0)
    hero = models.ManyToManyField(Hero, through='WeaponHero')
    damage = models.IntegerField(default=3)
    weapon_class = models.IntegerField(choices=WEAPON_CLASS, default=1)
    type = models.IntegerField(choices=WEAPON, default=1)
    number_of_attacks = models.IntegerField(default=0)


class WeaponHero(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name='weapons_hero')
    bought_weapons = models.ForeignKey(Weapon, on_delete=models.CASCADE, related_name='weapons_hero')
    selected = models.BooleanField(default=False)


class ArmorHero(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name='armor_hero')
    bought_armors = models.ForeignKey(Armor, on_delete=models.CASCADE, related_name='armor_hero')
    selected = models.BooleanField(default=False)
