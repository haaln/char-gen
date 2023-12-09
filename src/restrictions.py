import random

#def constraints(difficulty=0):
#    restrictionss = random.choice(account_type)
#    return restrictionss
def constraints(acc = True, goals = False, escape = False):
        restrictionss = []
        if acc:
                restrictionss.append("restriction:      " + random.choice(account_type))
        if goals:
                restrictionss.append("goal:             " + random.choice(goal))
        if escape:
                restrictionss.append("escape clause:    " + random.choice(escape_clause))
        return restrictionss


account_type = [
        "No restrictions.",
        "Skiller.",
        "OSaaT.",
        "Ironman.",
        "Hardcore Ironman.",
        "Ultimate Ironman.",
        "Ultimate Hardcore Ironman.",
        "Area restricted. (complete everything possible to move on to next area, backtrack whenever possible)",
        "Make a second character (no restrictions) alongside and progress equally in different paths.",
        "Bronzeman.",
        "PvP only.",
        "PvE only.",
        "Obtain the the BiS-items on your own without help.",
        "Equally progress in life skills as combat skills.",
        ]

goal = ["No explicit character objectives.",
        "Complete the entire game. (Completionist)",
        "Obtain a leaderboard rank in one aspect.",
        "Obtain rank 1 in any PvP setting.",
        "Obtain rank 1 in any PvE setting.",
        ]

escape_clause = [
        "There are no escape clauses.",
        "Achieve highest rank in anything.",
        "Complete all quests.",
        "Obtain one piece of the strongest equipment available.",
        "Explore/Unlock all of the world.",
        "Read and understand all the lore.",
        "Obtain the best mount.",
        "Obtain the rarest item in the game (within given ruleset).",
        ]
