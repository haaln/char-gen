#!/usr/bin/env python3

import random

def generate_restriction(restrict=None):
        if restrict:
                return random.choice(account_type)

def generate_goals(restrict=None, goals=None):
        if restrict:
                if goals:
                        return random.choice(goal)

def generate_esc_clause(restrict=None, escape=None):
        if restrict:
                if escape:
                        return random.choice(escape_clause)


account_type = [
        #"No restrictions.",
        "Skiller.",
        #"OSaaT (One Skil at a Time, where you must train chosen skill to the highest level before doing anything else)",
        "OSaaT",
        "Ironman.",
        "Hardcore Ironman.",
        "Ultimate Ironman.",
        "Ultimate Hardcore Ironman.",
        #"Area restricted. (complete everything possible to move on to next area, backtrack whenever possible)",
        "Area restricted.",
        #"Make a second character (no restrictions) alongside and progress equally in different paths.",
        "Make a second character (no restrictions).",
        "Bronzeman.",
        "PvP only.",
        "F2P+Ironman",
        "PvE only.",
        "Obtain the the Best-in-Slot items on your own without help.",
        "Equally progress in life skills as combat skills.",
        ]

goal = [#"No explicit character objectives.",
        "Complete the entire game. (Completionist)",
        "Obtain a leaderboard rank in one aspect.",
        "Obtain rank 1 in any PvP setting.",
        "Obtain rank 1 in any PvE setting.",
        ]

escape_clause = [
        #"There are no escape clauses.",
        "Achieve highest rank in anything.",
        "Complete all quests.",
        "Obtain one piece of the strongest equipment available.",
        "Explore/Unlock all of the world.",
        "Read and understand all the lore.",
        "Obtain the best mount.",
        "Obtain the rarest item in the game (within given ruleset).",
        ]

#if __name__ == '__main__':
#        for i in range(10):
#                print(generate_restrictions('character_restrictions','character_objective','character_esc_clause'))
