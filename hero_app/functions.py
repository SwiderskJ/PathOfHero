from random import randint
import math

def create_hero(hero):
    strenght_list = []

    for item in range(4):
        strenght_list.append(randint(1, 6))

    strenght_list.remove(min(strenght_list))

    strenght = 0
    for item in strenght_list:
        strenght += item
    if strenght < 6:
        strenght = 6
    hero.strength = strenght

    dexterity_list = []

    for item in range(4):
        dexterity_list.append(randint(1, 6))

    dexterity_list.remove(min(dexterity_list))

    dexterity = 0
    for item in dexterity_list:
        dexterity += item
    if dexterity < 6:
        dexterity = 6
    hero.dexterity = dexterity

    endurance_list = []

    for item in range(4):
        endurance_list.append(randint(1, 6))

    endurance_list.remove(min(endurance_list))

    endurance = 0
    for item in endurance_list:
        endurance += item
    if endurance < 6:
        endurance = 6
    hero.endurance = endurance

    intelligence_list = []

    for item in range(4):
        intelligence_list.append(randint(1, 6))

    intelligence_list.remove(min(intelligence_list))

    intelligence = 0
    for item in intelligence_list:
        strenght += item
    if intelligence < 6:
        intelligence = 6
    hero.intelligence = intelligence

    wisdom_list = []

    for item in range(4):
        wisdom_list.append(randint(1, 6))

    wisdom_list.remove(min(wisdom_list))

    wisdom = 0
    for item in wisdom_list:
        wisdom += item
    if wisdom < 6:
        wisdom = 6

    hero.wisdom = wisdom

    charisma_list = []

    for item in range(4):
        charisma_list.append(randint(1, 6))

    charisma_list.remove(min(charisma_list))

    charisma = 0
    for item in charisma_list:
        charisma += item
    if charisma < 6:
        charisma = 6
    hero.charisma = charisma

    # Generating race modification
    if hero.race == 2:
        hero.endurance += 2
        hero.charisma -= 2
    if hero.race == 3:
        hero.dexterity += 2
        hero.endurance -= 2
    if hero.race == 4:
        hero.endurance += 2
        hero.strength -= 2
    if hero.race == 6:
        hero.strength += 2
        hero.intelligence -= 2
        hero.charisma -= 2
    if hero.race == 7:
        hero.dexterity += 2
        hero.strength -= 2

    # Calculates various statistics for the hero.

    hero.strength_bonus = math.floor((hero.strength - 10) / 2)
    if hero.strength in [9, 10, 11]:
        hero.strength_bonus = 0
    elif hero.strength < 9:
        hero.strength_bonus = math.ceil((hero.strength - 10) / 2)

    hero.dexterity_bonus = math.floor((hero.dexterity - 10) / 2)
    if hero.dexterity in [9, 10, 11]:
        hero.dexterity_bonus = 0
    elif hero.dexterity < 9:
        hero.dexterity_bonus = math.ceil((hero.dexterity - 10) / 2)

    hero.endurance_bonus = math.floor((hero.endurance - 10) / 2)
    if hero.endurance in [9, 10, 11]:
        hero.endurance_bonus = 0
    elif hero.endurance < 9:
        hero.endurance_bonus = math.ceil((hero.endurance - 10) / 2)

    hero.intelligence_bonus = math.floor((hero.intelligence - 10) / 2)
    if hero.intelligence in [9, 10, 11]:
        hero.intelligence_bonus = 0
    elif hero.intelligence < 9:
        hero.intelligence_bonus = math.ceil((hero.intelligence - 10) / 2)

    hero.wisdom_bonus = math.floor((hero.wisdom - 10) / 2)
    if hero.wisdom in [9, 10, 11]:
        hero.wisdom_bonus = 0
    elif hero.wisdom < 9:
        hero.wisdom_bonus = math.ceil((hero.wisdom - 10) / 2)

    hero.charisma_bonus = math.floor((hero.charisma - 10) / 2)
    if hero.charisma in [9, 10, 11]:
        hero.charisma_bonus = 0
    elif hero.charisma < 9:
        hero.charisma_bonus = math.ceil((hero.charisma - 10) / 2)

    hero.max_health_points = round(12 + round(hero.level * 3) + hero.endurance_bonus)
    hero.health_points = hero.max_health_points

    hero.attack_bonus = hero.level + hero.strength_bonus
    hero.defence_bonus = hero.level + hero.dexterity_bonus
    hero.initiative = round((hero.intelligence_bonus + hero.wisdom_bonus + hero.charisma_bonus) / 3)
    hero.damage_bonus = hero.strength_bonus
    hero.damage = 3
    numbers_of_attacks = int(round(hero.level / 4))
    if numbers_of_attacks < 1:
        numbers_of_attacks = 1
    hero.number_of_attacks = int(round(hero.level / 4))
    hero.save()
