import random

#def constraints(difficulty=0):
#    restrictionss = random.choice(account_type)
#    return restrictionss
def constraints(acc = True, goals = False, escape = False):
        restrictionss = []
        if acc:
                restrictionss.append(random.choice(account_type))
        if goals:
                restrictionss.append(random.choice(goal))
        if escape:
                restrictionss.append(random.choice(escape_clause))
        return restrictionss


account_type = [
        "You have no restrictions.",
        "You are a skiller account.",
        "You are an OSaaT account.",
        "You are an Ironman account.",
        "You are a Hardcore Ironman account.",
        "You are an Ultimate Ironman account.",
        "You are an Ultimate Hardcore Ironman account.",
        "You are an area restricted account. (complete everything possible to move on to next area)",
        "You must make a second character (no restrictions) alongside your current and progress equally in different paths.",
        "You are a Bronze man.",
        "You are a PvP only account.",
        "You are a PvE only account."
        "Obtain the the BiS-items on your own without help.",
        "Equally progress in life skills as combat skills.",
        ]

goal = ["No explicit character objectives.",
        "Complete the entire game. (Completionist)",
        "Obtain a leaderboard rank in one aspect."
        ]

escape_clause = [
        "There are no escape clauses.",
        "Achieve highest rank in anything.",
        "Complete all quests.",
        "Obtain one piece of the strongest equipment available.",
        "Explore/Unlock all of the world.",
        "Read and understand all the lore.",
        "Obtain the best mount.",
        "Obtain the rarest item in the game (within given ruleset)."
        ]
