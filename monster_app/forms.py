from django import forms
from monster_app.models import EXPERIENCE


class MonsterForm(forms.Form):
    name = forms.CharField()
    strength = forms.IntegerField()
    dexterity = forms.IntegerField()
    endurance = forms.IntegerField()
    intelligence = forms.IntegerField()
    wisdom = forms.IntegerField()
    charisma = forms.IntegerField()
    max_health_points = forms.IntegerField()
    damage_reduction = forms.IntegerField()
    number_of_attacks = forms.IntegerField()
    damage = forms.IntegerField()
    initiative = forms.IntegerField()
    defence_bonus = forms.IntegerField()
    difficult = forms.IntegerField()
    experience = forms.ChoiceField(choices=EXPERIENCE)

