from django.db import models
from django.contrib.auth.models import User


class UserCurrency(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gold = models.IntegerField(default=100)
    diamonds = models.IntegerField(default=100)
