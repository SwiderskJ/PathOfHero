from django.db import models
DICE = (
    (1, "d3"),
    (2, "d4"),
    (3, "d6"),
    (4, "d8"),
    (5, "d10"),
    (6, "d12"),
    (7, "d20"),
)


class Monster(models.Model):
    name = models.CharField(max_length=16)
    level = models.IntegerField(default=1)
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    wisdom = models.IntegerField()
    endurance = models.IntegerField()
    health_points = models.IntegerField()
    max_health_points = models.IntegerField()
    difficult = models.IntegerField(null=True)
    damage_reduction = models.IntegerField(null=True)
    number_of_dices = models.IntegerField()
    dice = models.IntegerField(choices=DICE)
    damage = models.IntegerField(default=3)
    initiative = models.IntegerField(default=0)
