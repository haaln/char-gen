#!/usr/bin/env python3

import names
import backstory
import restrictions
import PySimpleGUI as sg

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


sg.set_options(text_justification='right')

layout = [ [sg.Text('Char-gen v.0.01')],
           [sg.Checkbox('First name'), sg.Checkbox('Surname')],
           [sg.Text('_' * 100, size=(65,1))],
           [sg.Text('Style')],
           [sg.Radio('Simple algorithm')],
           [sg.Radio('FFXIV')],
           [sg.Radio('Realistic')],
           [sg.Radio('Nickname')],
           [sg.Radio('Dwarf'), sg.Radio('Elf')],
           [sg.Text('_' * 100, size=(65,1))],
           [sg.CheckBox('Restrictions')],
           [sg.Checkbox('Backstory')],
           [sg.Submit(), sg.Cancel()] ]


window = sg.Window('character generator')

event, values = window.read()




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
