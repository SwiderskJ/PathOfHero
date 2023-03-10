# Generated by Django 4.1.6 on 2023-02-07 22:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Armor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=256)),
                ('defence_bonus', models.IntegerField()),
                ('attack_bonus', models.IntegerField()),
                ('damage_reduction', models.IntegerField()),
                ('price', models.IntegerField(default=0)),
                ('diamonds', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('race', models.IntegerField(choices=[(1, 'Human'), (2, 'Elf'), (3, 'Dwarf'), (4, 'Orc')])),
                ('experience_points', models.IntegerField(default=0)),
                ('level', models.IntegerField(default=0)),
                ('strength', models.IntegerField()),
                ('dexterity', models.IntegerField()),
                ('wisdom', models.IntegerField()),
                ('endurance', models.IntegerField()),
                ('health_points', models.IntegerField()),
                ('max_health_points', models.IntegerField()),
                ('is_alive', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=256)),
                ('defence_bonus', models.IntegerField()),
                ('attack_bonus', models.IntegerField()),
                ('damage_bonus', models.IntegerField()),
                ('price', models.IntegerField(default=0)),
                ('diamonds', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='WeaponHero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected', models.BooleanField(default=False)),
                ('bought_weapons', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hero_app.weapon')),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hero_app.hero')),
            ],
        ),
        migrations.AddField(
            model_name='weapon',
            name='hero',
            field=models.ManyToManyField(through='hero_app.WeaponHero', to='hero_app.hero'),
        ),
        migrations.CreateModel(
            name='ArmorHero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected', models.BooleanField(default=False)),
                ('bought_armors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hero_app.armor')),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hero_app.hero')),
            ],
        ),
        migrations.AddField(
            model_name='armor',
            name='hero',
            field=models.ManyToManyField(through='hero_app.ArmorHero', to='hero_app.hero'),
        ),
    ]
