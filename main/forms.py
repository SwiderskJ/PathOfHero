from django import forms
from main.models import HERO_RACE


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserCreateForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()


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


class WeaponAddForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()  #pytanie o format
    defence_bonus = forms.IntegerField()
    attack_bonus = forms.IntegerField()
    damage_bonus = forms.IntegerField()
    price = forms.IntegerField()
