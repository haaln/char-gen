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

sg.theme('Dark')
layout = [ [sg.Text('Char-gen v.0.01')],
           [sg.Text('Main', font=('Helvetica', 15))],
           [sg.Checkbox('First name'), sg.Checkbox('Surname')],
           [sg.Radio('Male', 1), sg.Radio('Female', 1)],
#          [sg.Checkbox('Show advanced settings')],
#          [sg.Checkbox('Length constraint'), sg.Spin(values=[i for i in range(1,16)], initial_value=9, size=(4,1))],
#          [sg.Checkbox('Exclude characters'), sg.InputText(size=(10,1))],
#          [sg.Checkbox('Include characters'), sg.InputText(size=(10,1))],
#          [sg.Checkbox('Allow spaces'), sg.Checkbox('Replace spaces with underscores')],
#          [sg.Checkbox('Begins with: '), sg.InputText(size=(10,1)), sg.Checkbox('Ends with: '), sg.InputText(size=(10,1))],
#          [sg.Radio('Manually choose name', 4)],
#          [sg.Checkbox('First name: '), sg.InputText(size=(10,1)), sg.Checkbox('Surname: '), sg.InputText(size=(10,1))],
#          [sg.Radio('generate similar to: ', 4), sg.Text('First name: '), sg.InputText(size=(10,1)), sg.Text('Last name: '), sg.InputText(size=(10,1))],
           [sg.Text('_' * 100, size=(65,1))],
           [sg.Text('Naming convention', font=('Helvetica', 15))],
           [sg.Radio('Fantasy', 2), sg.Radio('Human', 6), sg.Radio('Dwarven', 6), sg.Radio('Elven', 6)],
           [sg.Radio('FFXIV', 2), sg.Radio('Hyur', 3), sg.Radio('Lalafell', 3)],
           [sg.Radio('Nickname', 2)],
           [sg.Radio('Realistic', 2)],
#          [sg.Radio('Historic', 2)],
#          [sg.Radio('Nordic', 2)],
#          [sg.Radio('Greek / Roman', 2)],
#          [sg.Radio('Japanese', 2)],
#          [sg.Radio('Korean', 2)],
#          [sg.Radio('Chinese', 2)],
           [sg.Text('_' * 100, size=(65,1))],
           [sg.Text('Additional features', font=('Helvetica', 15))],
           # add conditional checkbox
           [sg.Checkbox('Character restrictions'), sg.Checkbox('Objectives'), sg.Checkbox('Escape clause')],
           [sg.Checkbox('Character backstory')],
#          [sg.Checkbox('Character portrait'), sg.Text('include tags: '), sg.InputText(size=(10,1)), sg.Text('exclude tags: '), sg.InputText(size=(10,1))],
           [sg.Text('_' * 100, size=(65,1))],
           #[sg.Text('Generate', size=(8, 1)), sg.Spin(values=[i for i in range(1, 21)], initial_value=1, size=(4, 1)), sg.Text('character(s).')],
           [sg.Button('Generate'), sg.Cancel()] ]

#layout_tabs = [
#                   [name('Tab, TabGroup'), sg.TabGroup([[sg.Tab('Tab1',[[sg.T(s=(15,2))]]), sg.Tab('Tab2', [[]])]])],]
#    [sg.TabGroup([sg.Tab('Main'),[sg.T(s=(15,2))], sg.Tab('Character'), sg.Tab('Backstory'), sg.Tab('Misc') )]] ]

window = sg.Window('character generator', layout)

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
