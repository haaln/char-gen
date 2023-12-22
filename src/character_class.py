#!/usr/bin/env python3

import random

def generate_class(game=None, sex=None, genderlock=None):
    if game:
        match game:
            case 'Black Desert':
                if genderlock:
                    match sex:
                        case 'male':
                            return random.choice(random.choice([bdo_character_male_class]))
                        case 'female':
                            return random.choice(random.choice([bdo_character_female_class]))
                else:
                    return random.choice(random.choice([bdo_character_class]))
            case 'FFXIV':
                return random.choice(random.choice([ffxiv_character_class]))
            case 'World of Warcraft':
                return random.choice(random.choice([wow_character_class]))
            case _:
                return random.choice(random.choice([generic_classes]))

    else:
        print('error, could not find class')

bdo_character_class = [ "Warrior", "Valkyrie", "Witch", "Wizard", 'Tamer', "Ranger", "Sorceress", "Berserker", "Musa", 'Maehwa', 'Ninja', 'Kunoichi', 'Dark Knight', 'Striker', 'Mystic', 'Lahn', 'Archer', 'Corsair', 'Drakania', 'Shai', 'Nova', 'Sage', 'Hashashin', 'Woosa', 'Maegu' ]
bdo_character_male_class = [ "Warrior", "Wizard", "Berserker", 'Ninja', 'Striker', 'Archer', 'Sage', 'Hashashin' ]
bdo_character_female_class = [ "Valkyrie", "Witch", 'Tamer', "Ranger", "Sorceress", 'Maehwa', 'Kunoichi', 'Dark Knight', 'Mystic', 'Lahn', 'Corsair', 'Drakania', 'Shai', 'Nova', 'Woosa', 'Maegu' ]
ffxiv_character_class = [ 'Gladiator', 'Marauder', 'Lancer', 'Pugilist', 'Rogue', 'Archer', 'Thaumaturge', 'Arcanist', 'Conjurer' ]
wow_character_class = [ 'Warrior', 'Paladin', 'Hunter', 'Rogue', 'Priest', 'Shaman', 'Mage', 'Warlock', 'Monk', 'Druid', 'Demon Hunter', 'Death Knight', 'Evoker' ]
generic_classes = [ 'Melee based', 'Ranged based', 'Magic based' ]

if __name__ == '__main__':
    for i in range(10):
        print(generate_class(game=random.choice(['Black Desert', 'FFXIV', 'World of Warcraft']), sex=random.choice(['male','female'])))
