import random

def character_background():
    story = \
        random.choice(origin) + " " +\
        random.choice(hobby)  + " " +\
        random.choice(achievement)
    return story

origin = [
         "You were born and raised in a hamlet.",
         "Your origins are unknown.",
         "You were born and raised on the battlefield."
         ]

hobby = [
        "You like drinking beer after a hard days of labor.",
        "You dislike dwarves.",
        "You loathe elves.",
        "You secretly like cats.",
        "You have a morbid quriosity towards certain indescretions."
        ]
achievement = [
                "Your greatest achievement is being able to remain standing in any drinking contest.",
                "Your most prideful moment was when you got away with stealing an apple from a child."
              ]
