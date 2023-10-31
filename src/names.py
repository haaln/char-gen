import random

def name():
    first_name = random.choice(male_prefix) + random.choice(male_suffix)
    surname = random.choice(surname_prefix) + random.choice(surname_suffix)
    name = first_name + ' ' + surname
    return name

male_prefix = [
                "Leo",
                "Ga",
                "Ra",
                "Ro",
                "Ha",
                "Ma",
                "Lo",
                "Bo",
                "Ko",
                "Ka",
                "Taur"
                ]

male_suffix = [
                "n",
                "do",
                "ndo",
                "nard",
                "io",
                "ius",
                "bo",
                ]

surname_prefix = [
                "Green",
                "Hawk",
                "Red",
                "Pierce",
                "River",
                "Wood",
                "Warren",
                "Gold"
                ]
surname_suffix = [
                "",
                "wood",
                "eye",
                "caller",
                "hammer",
                "runner",
                "berg",
                "burg"
                ]
