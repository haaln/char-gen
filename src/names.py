import random

#def name():
#    first_name = random.choice(male_prefix) + random.choice(male_suffix)
#    surname = random.choice(surname_prefix) + random.choice(surname_suffix)
#    name = first_name + ' ' + surname
#    return name
############################################################################
# type
#    fantasy (algorithm)
#    ffxiv
#    historic (greek/roman)
#    realistic (modern)
# race
#    elf
#    dwarf
#    human
#    esoteric
# sex
#    male
#    female
# length
#    3-16
# constraints
#    beginning
#    ending
#    spaces
#    special characters
#
############################################################################
def name(style=0, race=0, sex=0, constraints=None):
    given_name = first_name[sex][style]
    last_name = surname[style]
    return given_name + " " + last_name

male_prefix = ["Leo", "Ga", "Ra", "Ro", "Ha", "Ma", "Lo", "Go", "Vo", "Ko", "Ka"]
male_suffix = ["n", "nidas", "do", "ndo", "nard", "ius", "bo"]
female_prefix = [ "La", "Lu", "Yu", "Ra" ]
female_suffix = [ "ra", "ha", "na", "llie", "la" ]
female_ffxiv = ["Hemin", "Alicen", "Geva", "Gylda", "Motte", "Cecilia", "Amice", "Everill", "Edhida", "Lewena", "Mirabelle", "Aeditha", "Aldyet", "Audrye", "Aylufa", "Diamanda", "Eadburga", "Edda", "Edekin", "Edyva", "Eldid", "Elfleda", "Etfled", "Ethelinda", "Fryswyde", "Garthrite", "Gert", "Ginnade", "Godeleva", "Goodife", "Gudytha", "Hedheue", "Hida", "Hildeyerd", "Lefchild", "Lefleda", "Milburh", "Mildthryth", "Mydrede", "Osgyth", "Ositha", "Ostrythe", "Seburga", "Sungyve", "Synnove", "Theldry", "Urith", "Wulfiue", "Biddy", "Braya", "Eluned", "Emoni", "Essylt", "Fhlae", "Fuandrec", "Gloiucen", "Gloiumed", "Granae", "Guencen", "Guenguiu", "Ilcum", "Imania", "Jocea", "Lina", "Linyeve", "Meduil", "Merewina", "Airell", "Aislinn", "Allene", "Ceana", "Chaele", "Deidra", "Eara", "Eavan", "Edalene", "Eilis", "Fennella", "Fiachre", "Finnea", "Glynnis", "Ianna", "Keaira", "Keelty", "Keitha", "Maeve", "Meara", "Meriel", "Nuala", "Sileas", "Tieve", "Agnys", "Alainne", "Amelia", "Amphelice", "Angelet", "Anna", "Averil", "Ayleth", "Carmen"]
surname_prefix = ["Green", "Hawk", "Red", "Pierce", "River", "Wood", "Warren", "Gold" ]
surname_suffix = ["", "wood", "eye", "caller", "hammer", "runner", "berg", "shield", "stone", "guard", "stein", "man", "burg" ]
surname_ffxiv = ["Abbey", "Abel", "Ackerman", "Addock", "Allen", "Allond", "Arkwright", "Aubrey", "Bagley", "Ballard", "Barker", "Barlow", "Bell", "Bellveil", "Berry", "Bishop", "Braddock", "Brasher", "Brewer", "Broadbent", "Brooks", "Browne", "Carmine", "Carver", "Clarke", "Clay", "Clayworth", "Cooke", "Corwell", "Covey", "Dorne", "Dracht", "Eugene", "Goodman", "Fields", "Fisher", "Fletcher", "Fulke", "Gardner", "Gelson", "Glover", "Goode", "Goode", "Goodfellow", "Greave", "Greene", "Happer", "Hill", "Hodder", "Holmes", "Holt", "Hunt", "Jeanne", "Kirkmann", "Lannis", "Leach", "Leatherby", "Lee", "Little", "Mason", "Meath", "Mercer", "Miller", "Moore", "Morning", "Newton", "Nolan", "North", "Oswell", "Piper", "Poole", "Potter", "Reed", "Rich", "Rose", "Sadler", "Sawyer", "Shepard", "Slater", "Smith", "Southway", "Spence", "Stark", "Tanner", "Walker", "Ward", "Weild", "West", "White", "Winsome", "Witte", "Yaeger", "Yar", "Yarborough", "Weaver", "Webb", "Wells", "Wheeler", "Wright", "Young" ]
male_ffxiv = ["Anselmet", "Clerebold", "Lodewicus", "Talan", "Aldous", "Abraham", "Mansel", "Werner", "Powle", "Albin", "Arthur", "Augustine", "Bayard", "Belmont", "Benedict", "Beneger", "Boyle", "Bran", "Bruce", "Clifton", "Clive", "Colbert", "Colson", "Conphas", "Cornell", "Coster", "Cyriac", "Daimbert", "Dalmas", "Danyell", "Deitrich", "Denston", "Derwin", "Deryk", "Eleazar", "Emanuel", "Erasmus", "Erik", "Esmond", "Esmour", "Esperaunce", "Etgar", "Frederyk", "Geoffrey", "Gerald", "Gerbold", "Guston", "Gwayne", "Gylbart", "Halstein", "Hewrey", "Hoddyn", "Humphrey", "Johannes", "Jonathas", "Joseph", "Kennard", "Kerrich", "Kinnison", "Ladislas", "Lambert", "Laurence", "Laurentius", "Lodwicke", "Madison", "Mainfroi", "Mathye", "Mordyn", "Morgant", "Morys", "Navarre", "Noes", "Olyver", "Orisic", "Orrick", "Orwen", "Osric", "Raffe", "Rauffe", "Raulin", "Ribald", "Ricard", "Rickeman", "Roarich", "Robyn", "Roger", "Rothe", "Roundelph", "Rowland", "Rycharde", "Samson", "Sandre", "Sigurdh", "Simond", "Templeton", "Vannes", "Vyncent", "Voyce", "Willielmus", "Wineburg"]

fantasy =  [ random.choice(male_prefix)+random.choice(male_suffix), random.choice(female_prefix)+random.choice(female_suffix) ]
male_firstname = [ random.choice(male_ffxiv), random.choice(male_prefix)+random.choice(male_suffix) ]
female_firstname = [ random.choice(female_ffxiv), random.choice(female_prefix)+random.choice(female_suffix) ]
first_name = [ male_firstname, female_firstname ]
surname = [ random.choice(surname_prefix)+random.choice(surname_suffix), random.choice(surname_ffxiv) ]
