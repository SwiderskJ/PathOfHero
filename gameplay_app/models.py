from django.db import models
from django.template.defaultfilters import slugify
from hero_app.models import Hero
import datetime
from random import randint

EVENTS = (
    (1, "One-way tunnel"),
    (2, "Cross"),
    (3, "End of tunel"),
    (4, "Boss"),
)


class Maze(models.Model):
    position = models.IntegerField()
    events = models.IntegerField(choices=EVENTS, null=True, default=1)
    difficulty = models.IntegerField(default=0)
    hero = models.ManyToManyField(Hero, through='MazeHero')
    slug = models.CharField(max_length=200, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.position) + str(randint(1, 1000)) + " " + str(int(datetime.datetime.now().timestamp())))
        return super().save(*args, **kwargs)


class MazeHero(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    position = models.ForeignKey(Maze, on_delete=models.CASCADE)
    last_position = models.IntegerField(default=1)
    active_position = models.BooleanField(default=True)
