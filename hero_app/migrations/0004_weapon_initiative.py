# Generated by Django 4.1.6 on 2023-02-08 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero_app', '0003_hero_damage_weapon_damage'),
    ]

    operations = [
        migrations.AddField(
            model_name='weapon',
            name='initiative',
            field=models.IntegerField(default=0),
        ),
    ]