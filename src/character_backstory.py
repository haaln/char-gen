import random

# add dreams/hopes backstory
# human city backstory

def generate_background() -> str:
    story =     random.choice(origin)\
        + ' ' + random.choice(fact)\
        + " " + random.choice(achievement)
    return story

origin = ["You were born and raised in a hamlet.",
         "Your origins are unknown.",
         "Your origins are unknown.",
         "You were born and raised on the battlefield." ]

fact = ["You like drinking beer after a hard days of labor.",
        "You dislike dwarves.",
        "You dislike elves.",
        "You are a member of a secret society.",
        "You are allergic to books.",
        "You secretly like cats.",
        "You have a morbid quriosity towards forbidden knowledge."]

dislike = [ "Elves", "Humans", "Dwarves", "noise", "rowdy places", "dishonesty" ]

trait = [ "agile", "witty", "simple", "honest", "taciturn", "crafty", "pragmatic", "utilitarian" ]

achievement = ["Your greatest skill is being able to remain standing in any drinking contest.",
               "You have never been defeated in a game of dice.",
               "Your greatest achievement was when you won a stare down against a stray dog.",
               "Your most prideful moment was when you bested a blind man in a bar fight."]

exposition = [ "You have a serious dislike for DISLIKE",
               "You are TRAIT",
               "You are from CITY",
               random.choice(fact),
               random.choice(achievement),
               random.choice(origin) ]

dwarf_city = [ "Gorndarum", "Birnkahldur", "Hig Faldir", "Bhom Buldor", "Haggrim", "Dugbihr", "Gol Durahl", "Bhogh Darohm", "Thoghbuldahr", "Veglodahr", "Kan Taruhm", "Ham Darul", "Vern Darim" ]
elf_city = [ "Amyenshys", "Shylve Entheas", "Emflin", "Amyfrion", "Mfe Asari", "Ellon", "Ins Lenora", "Emi Alora", "Onle Taesi", "Wailin", "Efan Esari" ]
