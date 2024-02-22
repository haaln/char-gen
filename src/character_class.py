#!/usr/bin/env python3

import random

def generate_class(game=None, sex=None, genderlock=None):
    if game:
        if game == 'Black Desert':
            if genderlock:
                if sex == 'male':
                    return random.choice(random.choice([bdo_character_male_class]))
                if sex == 'female':
                    return random.choice(random.choice([bdo_character_female_class]))
            else:
                return random.choice(random.choice([bdo_character_class]))
        if game == 'FFXIV':
            return random.choice(random.choice([ffxiv_character_class]))
        if game ==  'World of Warcraft':
            return random.choice(random.choice([wow_character_class]))
        else:
            return random.choice(random.choice([generic_classes]))

bdo_character_class = [ "Warrior", "Valkyrie", "Witch", "Wizard", 'Tamer', "Ranger", "Sorceress", "Berserker", "Musa", 'Maehwa', 'Ninja', 'Kunoichi', 'Dark Knight', 'Striker', 'Mystic', 'Lahn', 'Archer', 'Corsair', 'Drakania', 'Shai', 'Nova', 'Sage', 'Hashashin', 'Woosa', 'Maegu' ]
bdo_character_male_class = [ "Warrior", "Wizard", "Berserker", 'Ninja', 'Striker', 'Archer', 'Sage', 'Hashashin' ]
bdo_character_female_class = [ "Valkyrie", "Witch", 'Tamer', "Ranger", "Sorceress", 'Maehwa', 'Kunoichi', 'Dark Knight', 'Mystic', 'Lahn', 'Corsair', 'Drakania', 'Shai', 'Nova', 'Woosa', 'Maegu' ]
ffxiv_character_class = [ 'Gladiator', 'Marauder', 'Lancer', 'Pugilist', 'Rogue', 'Archer', 'Thaumaturge', 'Arcanist', 'Conjurer' ]
wow_character_class = [ 'Warrior', 'Paladin', 'Hunter', 'Rogue', 'Priest', 'Shaman', 'Mage', 'Warlock', 'Monk', 'Druid', 'Demon Hunter', 'Death Knight', 'Evoker' ]
generic_classes = [ 'Melee based', 'Ranged based', 'Magic based' ]

if __name__ == '__main__':
    for i in range(10):
        print(generate_class(game=random.choice(['Black Desert', 'FFXIV', 'World of Warcraft']), sex=random.choice(['male','female'])))
