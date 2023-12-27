#!/usr/bin/env python3

import random

def generate_restriction():
        return random.choice(account_type)

def generate_goals():
        return random.choice(goal)

def generate_esc_clause():
        return random.choice(escape_clause)


account_type = [
        "Skiller",
        "OSaaT",
        "Ironman",
        "Hardcore Ironman",
        "Hardcore",
        "Ultimate Ironman",
        "Ultimate Hardcore Ironman",
        #"Area restricted. (complete everything possible to move on to next area, backtrack whenever possible)",
        "Area restricted",
        "Make a second character (no restrictions) alongside and progress equally in different paths.",
        "Bronzeman",
        "PvP only",
        "PvE only",
        "Obtain the the Best-in-Slot items on your own without help",
        "Equally progress in skilling and combat",
        ]

goal = [
        "Complete the entire game. (Completionist)",
        "Obtain a leaderboard rank in one aspect.",
        "Obtain rank 1 in any PvP setting",
        "Obtain rank 1 in any PvE setting",
        ]

escape_clause = [
        "Achieve rank #1 in anything",
        "Achieve highest level in anything",
        "Collect all treasure items",
        "Complete all quests",
        "Obtain one piece of the strongest equipment available",
        "Explore/Unlock all of the world",
        "Read and understand all the lore",
        "Obtain the best mount",
        "Obtain the rarest item in the game (within given ruleset)",
        ]

if __name__ == '__main__':
        for i in range(10):
                print(generate_restriction())
                print(generate_goals())
                print(generate_esc_clause())
                print("\n")
