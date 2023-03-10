# Generated by Django 4.1.6 on 2023-02-12 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero_app', '0010_weapon_type_weapon_weapon_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weapon',
            name='type',
            field=models.IntegerField(choices=[(1, 'Attack without weapon'), (2, 'light melee weapon'), (3, 'One-handed combat weapon'), (4, 'A two-handed melee weapon')], default=1),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='weapon_class',
            field=models.IntegerField(choices=[(1, 'Simple Weapons'), (2, "Soldier's weapon"), (3, 'Exotic weapons')], default=1),
        ),
    ]
