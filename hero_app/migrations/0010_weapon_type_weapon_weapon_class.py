# Generated by Django 4.1.6 on 2023-02-12 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero_app', '0009_remove_armor_attack_bonus_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='weapon',
            name='type',
            field=models.IntegerField(choices=[(1, 'Attack without weapon'), (2, 'light melee weapon'), (3, 'One-handed combat weapon'), (4, '')], default=1),
        ),
        migrations.AddField(
            model_name='weapon',
            name='weapon_class',
            field=models.IntegerField(choices=[(1, 'Simple Weapons')], default=1),
        ),
    ]
