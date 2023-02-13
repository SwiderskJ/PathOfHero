import math
from django.template.defaultfilters import slugify
from random import randint
from django.db import models


EXPERIENCE = (
    (1, 5400),
    (2, 3600),
    (3, 2700),
    (4, 1800),
    (5, 1350),
    (6, 900),
    (7, 600),
    (8, 300),
)


class Monster(models.Model):
    name = models.CharField(max_length=16)
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    endurance = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()
    health_points = models.IntegerField(default=0)
    max_health_points = models.IntegerField(default=0)
    difficult = models.IntegerField(null=True)
    damage_reduction = models.IntegerField(null=True)
    number_of_attacks = models.IntegerField()
    damage = models.IntegerField(default=3)
    initiative = models.IntegerField(default=0)
    attack_bonus = models.IntegerField(default=0)
    defence_bonus = models.IntegerField(default=0)
    damage_bonus = models.IntegerField(default=0)
    experience = models.IntegerField(choices=EXPERIENCE)
    prize = models.IntegerField(default=0)
    strength_bonus = models.IntegerField(default=0)
    dexterity_bonus = models.IntegerField(default=0)
    endurance_bonus = models.IntegerField(default=0)
    intelligence_bonus = models.IntegerField(default=0)
    wisdom_bonus = models.IntegerField(default=0)
    charisma_bonus = models.IntegerField(default=0)
    slug = models.CharField(max_length=200, unique=True, default=0)

    def save(self, *args, **kwargs):
        self.health_points = self.max_health_points

        self.strength_bonus = math.floor((self.strength - 10) / 2)
        if self.strength in [9, 10, 11]:
            self.strength_bonus = 0
        elif self.strength < 9:
            self.strength_bonus = math.ceil((self.strength - 10) / 2)

        self.dexterity_bonus = math.floor((self.dexterity - 10) / 2)
        if self.dexterity in [9, 10, 11]:
            self.dexterity_bonus = 0
        elif self.dexterity < 9:
            self.dexterity_bonus = math.ceil((self.dexterity - 10) / 2)

        self.endurance_bonus = math.floor((self.endurance - 10) / 2)
        if self.endurance in [9, 10, 11]:
            self.endurance_bonus = 0
        elif self.endurance < 9:
            self.endurance_bonus = math.ceil((self.endurance - 10) / 2)

        self.intelligence_bonus = math.floor((self.intelligence - 10) / 2)
        if self.intelligence in [9, 10, 11]:
            self.intelligence_bonus = 0
        elif self.intelligence < 9:
            self.intelligence_bonus = math.ceil((self.intelligence - 10) / 2)

        self.wisdom_bonus = math.floor((self.wisdom - 10) / 2)
        if self.wisdom in [9, 10, 11]:
            self.wisdom_bonus = 0
        elif self.wisdom < 9:
            self.wisdom_bonus = math.ceil((self.wisdom - 10) / 2)

        self.charisma_bonus = math.floor((self.charisma - 10) / 2)
        if self.charisma in [9, 10, 11]:
            self.charisma_bonus = 0
        elif self.charisma < 9:
            self.charisma_bonus = math.ceil((self.charisma - 10) / 2)
        self.attack_bonus = self.strength_bonus
        self.damage_bonus = self.strength_bonus
        if self.slug == 0:
            self.slug = slugify(self.name + str(randint(1, 1000)) + str(self.strength) +
                                str(self.dexterity) + str(randint(1, 1000)))
        self.prize = round(randint(1, 10) * self.damage)
        return super().save(*args, **kwargs)
