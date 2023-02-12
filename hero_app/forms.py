from django import forms
from hero_app.models import HERO_RACE, WEAPON_CLASS, WEAPON, ARMOR


class CreateHeroForm(forms.Form):
    name = forms.CharField()
    race = forms.ChoiceField(choices=HERO_RACE)


class ArmorAddForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    defence_bonus = forms.IntegerField()
    damage_reduction = forms.IntegerField()
    price = forms.IntegerField()
    diamonds = forms.IntegerField()
    type = forms.ChoiceField(choices=ARMOR)


class WeaponAddForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    attack_bonus = forms.IntegerField()
    damage_bonus = forms.IntegerField()
    damage = forms.IntegerField()
    price = forms.IntegerField()
    diamonds = forms.IntegerField()
    weapon_class = forms.ChoiceField(choices=WEAPON_CLASS)
    type = forms.ChoiceField(choices=WEAPON)
    number_of_attacks = forms.IntegerField()
