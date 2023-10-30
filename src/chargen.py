#!/usr/bin/env python3
import random

import names
import backstory
import restrictions



def character_background():
    story = \
        random.choice(backstory.origin) + " " +\
        random.choice(backstory.hobby)  + " " +\
        random.choice(backstory.achievement)
    return story

def constraints(difficulty=0):
    restrictionss = random.choice(restrictions.account_type)
    return restrictionss

def goals():
    return

def name():
    first_name = random.choice(names.male_prefix) + random.choice(names.male_suffix)
    surname = random.choice(names.surname_prefix) + random.choice(names.surname_suffix)
    name = first_name + ' ' + surname
    return name

def im_gen():
    return

#first_name = r_beginning + r_ending
if __name__ == '__main__':
    print(name())
    print(constraints())
    print(character_background())

class Character:
    def __init__(self, sex='male', first_name='John', surname='Doe', backstory=character_background()):
        self._name = name
        self._surname = surname
        self._sex = sex
        self._backstory = backstory

class Restrictions:
    def __init__(self):
        self._osaat = None
        self._skiller = None
        self._f2p = None
        self._ironman = None
        self._hardcore_ironman = None

class Goals:
    def __init__(self):
        self._gather = None
        self._combat = None
        self._crafting = None
        self._completionist = None
