from django.db import models
from django.contrib.auth.models import User

HERO_RACE = (
    (1, "Human"),
    (2, "Elf"),
    (3, "Dwarf"),
    (4, "Orc"),
)


class Hero(models.Model):
    name = models.CharField(max_length=16)
    race = models.IntegerField(choices=HERO_RACE)
    experience_points = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    wisdom = models.IntegerField()
    endurance = models.IntegerField()
    health_points = models.IntegerField()
    max_health_points = models.IntegerField()
    is_alive = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attack_bonus = models.IntegerField(default=0)
    defence_bonus = models.IntegerField(default=0)
    damage_reduction = models.IntegerField(default=0)
    damage_bonus = models.IntegerField(default=0)
    damage = models.IntegerField(default=3)
    initiative = models.IntegerField(default=0)


class Armor(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    defence_bonus = models.IntegerField()
    attack_bonus = models.IntegerField()
    damage_reduction = models.IntegerField()
    price = models.IntegerField(default=0)
    diamonds = models.IntegerField(default=0)
    hero = models.ManyToManyField(Hero, through='ArmorHero')


class Weapon(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    defence_bonus = models.IntegerField()
    attack_bonus = models.IntegerField()
    damage_bonus = models.IntegerField()
    price = models.IntegerField(default=0)
    diamonds = models.IntegerField(default=0)
    hero = models.ManyToManyField(Hero, through='WeaponHero')


class WeaponHero(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name='weapons_hero')
    bought_weapons = models.ForeignKey(Weapon, on_delete=models.CASCADE, related_name='weapons_hero')
    selected = models.BooleanField(default=False)


class ArmorHero(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name='armor_hero')
    bought_armors = models.ForeignKey(Armor, on_delete=models.CASCADE, related_name='armor_hero')
    selected = models.BooleanField(default=False)
