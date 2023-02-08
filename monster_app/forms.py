from django import forms
from models import DICE


class Monster(forms.Form):
    name = forms.CharField()
    description = forms.TextInput()
    level = forms.IntegerField()
    strength = forms.IntegerField()
    dexterity = forms.IntegerField()
    wisdom = forms.IntegerField()
    endurance = forms.IntegerField()
    health_points = forms.IntegerField()
    max_health_points = forms.IntegerField()
    difficult = forms.IntegerField()
    damage_reduction = forms.IntegerField()
    number_of_dices = forms.IntegerField()
    dice = forms.ChoiceField(choices=DICE)

