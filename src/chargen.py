#!/usr/bin/env python3
import random

import names
import backstory
import restrictions

def goals():
    return

def im_gen():
    return

if __name__ == '__main__':
    print(names.name())
    print(restrictions.constraints())
    print(backstory.character_background())

class Character:
    def __init__(self, sex='male', first_name='John', surname='Doe', backstory=backstory.character_background()):
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
