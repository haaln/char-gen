import random

def generate_class(game:str, sex:str, genderlock:bool) -> str:
    if game == 'Black Desert':
        if genderlock:
            if sex == 'male':
                return random.choice(random.choice([bdo_character_male_class]))
            if sex == 'female':
                return random.choice(random.choice([bdo_character_female_class]))
        else:
            return random.choice(random.choice([bdo_character_class]))
    elif game == 'FFXIV':
        return random.choice(random.choice([ffxiv_character_class]))
    elif game ==  'World of Warcraft':
        return random.choice(random.choice([wow_character_class]))

    return random.choice(random.choice([generic_classes]))


bdo_character_class = [ "Warrior", "Valkyrie", "Witch", "Wizard", 'Tamer', "Ranger", "Sorceress", "Berserker", "Musa", 'Maehwa', 'Ninja', 'Kunoichi', 'Dark Knight', 'Striker', 'Mystic', 'Lahn', 'Archer', 'Corsair', 'Drakania', 'Shai', 'Nova', 'Sage', 'Hashashin', 'Woosa', 'Maegu' ]
bdo_character_male_class = [ "Warrior", "Wizard", "Berserker", 'Ninja', 'Striker', 'Archer', 'Sage', 'Hashashin' ]
bdo_character_female_class = [ "Valkyrie", "Witch", 'Tamer', "Ranger", "Sorceress", 'Maehwa', 'Kunoichi', 'Dark Knight', 'Mystic', 'Lahn', 'Corsair', 'Drakania', 'Shai', 'Nova', 'Woosa', 'Maegu' ]
ffxiv_character_class = [ 'Gladiator', 'Marauder', 'Lancer', 'Pugilist', 'Rogue', 'Archer', 'Thaumaturge', 'Arcanist', 'Conjurer' ]
wow_character_class = [ 'Warrior', 'Paladin', 'Hunter', 'Rogue', 'Priest', 'Shaman', 'Mage', 'Warlock', 'Monk', 'Druid', 'Demon Hunter', 'Death Knight', 'Evoker' ]
generic_classes = [ 'Melee based', 'Ranged based', 'Magic based' ]
