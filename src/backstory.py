import random

# add dreams/hopes backstory
# human city backstory


def character_background():
    story = \
        random.choice(origin) + " " +\
        random.choice(hobby)  + " " +\
        random.choice(achievement)
    return story

origin = ["You were born and raised in a hamlet.",
         "Your origins are unknown.",
         "You were born and raised on the battlefield." ]


hobby = ["You like drinking beer after a hard days of labor.",
        "You dislike dwarves.",
        "You loathe elves.",
        "You secretly like cats.",
        "You have a morbid quriosity towards certain indescretions."]
dislike = [ "Elves", "Humans", "Dwarves", "noise", "rowdy places", "dishonesty" ]
trait = [ "agile", "witty", "simple", "honest", "taciturn", "crafty", "pragmatic", "utilitarian" ]
achievement = ["Your greatest achievement is being able to remain standing in any drinking contest.",
               "Your most prideful moment was when you got away with stealing an apple from a child."]

exposition = [ "You have a serious dislike for DISLIKE",
               "You are TRAIT",
               "You are from CITY",
               random.choice(hobby),
               random.choice(achievement),
               random.choice(origin) ]

dwarf_city = [ "Gorndarum", "Birnkahldur", "Hig Faldir", "Bhom Buldor", "Haggrim", "Dugbihr", "Gol Durahl", "Bhogh Darohm", "Thoghbuldahr", "Veglodahr", "Kan Taruhm", "Ham Darul", "Vern Darim" ]
elf_city = [ "Amyenshys", "Shylve Entheas", "Emflin", "Amyfrion", "Mfe Asari", "Ellon", "Ins Lenora", "Emi Alora", "Onle Taesi", "Wailin", "Efan Esari" ]
