from django.db import models

DICE = (
    (1, 3),
    (2, 4),
    (3, 6),
    (4, 8),
    (5, 10),
    (6, 12),
    (7, 20),
)


class Monster(models.Model):
    name = models.CharField(max_length=16)
    level = models.IntegerField(default=1)
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    wisdom = models.IntegerField()
    endurance = models.IntegerField()
    health_points = models.IntegerField(default=0)
    max_health_points = models.IntegerField(default=0)
    difficult = models.IntegerField(null=True)
    damage_reduction = models.IntegerField(null=True)
    number_of_dices = models.IntegerField()
    dice = models.IntegerField(choices=DICE)
    damage = models.IntegerField(default=3)
    initiative = models.IntegerField(default=0)
    attack_bonus = models.IntegerField(default=0)
    defence_bonus = models.IntegerField(default=0)
    damage_bonus = models.IntegerField(default=0)
    slug = models.CharField(max_length=200, unique=True, default=0)


