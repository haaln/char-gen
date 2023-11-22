import random

# add optional escape clause for goal/account type

def constraints(difficulty=0):
    restrictionss = random.choice(account_type)
    return restrictionss

account_type = [
        "You are a skiller account.",
        "You are an OSaaT account."
        "You are a main account.",
        "You are an Ironman account.",
        "You are a Hardcore Ironman account.",
        "You are an Ultimate Ironman account.",
        "You are an Ultimate Hardcore Ironman account."
        "You are a Bronze man."
        ]

goal = [ "You must equally progress in life skills as combat skills.",
         "You must obtain half of all your items on your own.",
         "You must complete any quest that you come accross.",
         "You must obtain a leaderboard rank in one aspect.",
         "You must complete everything possible in one area before you may unlock a new area previously not visited",
         "You must make a second character alongside your current and progress equally in different paths." ]
