# Generated by Django 4.1.6 on 2023-02-06 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_armor_heroequipment_weapon_heroequipment_weapon_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='armor',
            name='hero',
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='hero',
        ),
        migrations.DeleteModel(
            name='HeroEquipment',
        ),
    ]
