# Generated by Django 4.1.6 on 2023-02-08 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monster_app', '0003_alter_monster_damage_reduction_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monster',
            name='description',
        ),
    ]
