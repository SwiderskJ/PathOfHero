from django import forms
from monster_app.models import DICE


class MonsterForm(forms.Form):
    name = forms.CharField()
    level = forms.IntegerField()
    strength = forms.IntegerField()
    dexterity = forms.IntegerField()
    wisdom = forms.IntegerField()
    endurance = forms.IntegerField()
    max_health_points = forms.IntegerField()
    difficult = forms.IntegerField()
    damage_reduction = forms.IntegerField()
    number_of_dices = forms.IntegerField()
    dice = forms.ChoiceField(choices=DICE)

