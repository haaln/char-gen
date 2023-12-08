#!/usr/bin/env python3

import names
import backstory
import restrictions

def goals():
    return

def im_gen():
    return

if __name__ == '__main__':
    for i in range(1,10):
        print(names.generate_firstname() + " " + names.generate_surname())
        rs = restrictions.constraints(True,True,True)
        for i in range(0,len(rs)):
            print(rs[i])
#   print(backstory.character_background())
        print("\n")











# kind of unnecessary when there is no generation-name or fitness randomization
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
