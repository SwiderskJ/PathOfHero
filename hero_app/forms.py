from django import forms
from hero_app.models import HERO_RACE


class CreateHeroForm(forms.Form):
    name = forms.CharField()
    race = forms.ChoiceField(choices=HERO_RACE)
    strength = forms.IntegerField()
    dexterity = forms.IntegerField()
    wisdom = forms.IntegerField()
    endurance = forms.IntegerField()


class ArmorAddForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    defence_bonus = forms.IntegerField()
    attack_bonus = forms.IntegerField()
    damage_reduction = forms.IntegerField()
    price = forms.IntegerField()
    diamonds = forms.IntegerField()


class WeaponAddForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()  # ask about format
    defence_bonus = forms.IntegerField()
    attack_bonus = forms.IntegerField()
    damage_bonus = forms.IntegerField()
    price = forms.IntegerField()
    diamonds = forms.IntegerField()
