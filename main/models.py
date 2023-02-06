from django.db import models
from django.contrib.auth.models import User
# Create your models here.
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
    level = models.IntegerField(default=0)
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    wisdom = models.IntegerField()
    endurance = models.IntegerField()
    health_points = models.IntegerField()
    max_health_points = models.IntegerField()
    is_alive = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Armor(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    defence_bonus = models.IntegerField()
    attack_bonus = models.IntegerField()
    damage_reduction = models.IntegerField()
    price = models.IntegerField()


class Weapon(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    defence_bonus = models.IntegerField()
    attack_bonus = models.IntegerField()
    damage_bonus = models.IntegerField()
    price = models.IntegerField()


# request.
# class HeroEquipment(models.Model):
#     hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
#     armor = models.ForeignKey(Armor, on_delete=models.CASCADE)
#     weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE)


