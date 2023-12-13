#!/usr/bin/env python3

import names
import backstory
import restrictions
import character_class
import PySimpleGUI as sg

sg.set_options(text_justification='right')

sg.theme('Dark')
layout = [[sg.Text('Character generator')],
          [sg.Text('Main', font=('Helvetica', 15))],
          [sg.Checkbox('First name', default=True, key='firstname'), sg.Checkbox('Surname', default=True, key='surname')],
          [sg.Radio('Male', 1, default=True, key=('male', 'sex')), sg.Radio('Female', 1, key=('female', 'sex'))],
#         [sg.Checkbox('Enable advanced settings', enable_events=True, key='advanced_options')],
#         [sg.Checkbox('Length constraint', key='length_constraint', enable_events=True, disabled=True), sg.Spin(values=[i for i in range(1,16)], initial_value=9, size=(4,1), key='length_spinner', enable_events=True, disabled=True)],
#         [sg.Checkbox('Exclude characters',key='exclude_char_checkbox', enable_events=True, disabled=True), sg.InputText(size=(10,1),key='exclude_char_input', enable_events=True, disabled=True)],
#         [sg.Checkbox('Include characters',key='include_char_checkbox', enable_events=True, disabled=True), sg.InputText(size=(10,1),key='include_char_input',enable_events=True, disabled=True)],
#         [sg.Checkbox('Allow spaces', key='allow_spaces', enable_events=True, disabled=True), sg.Checkbox('Replace spaces with underscores', key='replace_space_underscore', enable_events=True, disabled=True)],
#         [sg.Checkbox('Begins with: '), sg.InputText(size=(10,1)), sg.Checkbox('Ends with: '), sg.InputText(size=(10,1))],
#         [sg.Radio('Manually choose name', 4)],
#         [sg.Checkbox('First name: '), sg.InputText(size=(10,1)), sg.Checkbox('Surname: '), sg.InputText(size=(10,1))],
#         [sg.Radio('generate similar to: ', 4), sg.Text('First name: '), sg.InputText(size=(10,1)), sg.Text('Last name: '), sg.InputText(size=(10,1))],
          [sg.Text('_' * 100, size=(65,1))],
          [sg.Text('Naming convention', font=('Helvetica', 15))],
          [sg.Radio('Simple', 2, default=True, key=('simple', 'style'), enable_events=True)],
#         [sg.Radio('Tolkien', 2), sg.Radio('Human', 6), sg.Radio('Dwarven', 6), sg.Radio('Elven', 6)],
          [sg.Radio('FFXIV', 2, key='ffxiv', enable_events=True),\
               sg.Radio('Hyur', 3, disabled=True, default=True, key=('ffxiv_hyur','style')),\
               sg.Radio('Lalafell', 3, disabled=True, key=('ffxiv_lala','style')),\
               sg.Radio('Au Ra', 3, disabled=True, key=('ffxiv_aura','style')),\
               sg.Radio("Miqo'te", 3, disabled=True, key=('ffxiv_miqote', 'style'))],
          [sg.Radio('Nickname', 2, key=('nickname', 'style'), enable_events=True)],
          [sg.Radio('Realistic', 2, key=('realistic', 'style'), enable_events=True)],
#         [sg.Radio('Historic', 2)],
#         [sg.Radio('Nordic', 2)],
#         [sg.Radio('Greek / Roman', 2)],
#         [sg.Radio('Japanese', 2)],
#         [sg.Radio('Korean', 2)],
#         [sg.Radio('Chinese', 2)],
          [sg.Text('_' * 100, size=(65,1))],
          [sg.Text('Additional features', font=('Helvetica', 15))],
          [sg.Checkbox('Character restrictions', key=('character_restrictions', 'restrictions'), enable_events=True, tooltip=' Generate a character restriction such as Ironman mode '), \
               sg.Checkbox('Objectives', tooltip=' Provides a random goal to achieve with this character ', key=('character_objectives', 'restrictions'), disabled=True), \
               sg.Checkbox('Escape clause', tooltip=' Allow a condition where if fulfilled, you may forego your character restriction ', key=('character_esc_clause', 'restrictions'), disabled=True)],
          [sg.Checkbox('Character backstory', key='character_backstory')],
          [sg.Checkbox('Character class', key='character_class', enable_events=True, tooltip=' Picks a random class for the character depending on game '), \
               sg.Combo(values=['Black Desert', 'FFXIV', 'World of Warcraft', 'Unspecified'], default_value=['Unspecified'], disabled=True, enable_events=True, key='character_class_combo', readonly=True)],
#         [sg.Checkbox('Character portrait'), sg.Text('include tags: '), sg.InputText(size=(10,1)), sg.Text('exclude tags: '), sg.InputText(size=(10,1))],
          [sg.Text('_' * 100, size=(65,1))],
          #[sg.Text('Generate', size=(8, 1)), sg.Spin(values=[i for i in range(1, 21)], initial_value=1, size=(4, 1)), sg.Text('character(s).')],
          [sg.Button('Generate', enable_events=True, key='generate'), sg.Cancel(key='cancel')] ]

#layout_tabs = [
#                   [name('Tab, TabGroup'), sg.TabGroup([[sg.Tab('Tab1',[[sg.T(s=(15,2))]]), sg.Tab('Tab2', [[]])]])],]
#    [sg.TabGroup([sg.Tab('Main'),[sg.T(s=(15,2))], sg.Tab('Character'), sg.Tab('Backstory'), sg.Tab('Misc') )]] ]

window = sg.Window('character generator', layout)

while True:
    event, values = window.read()

    if values['ffxiv'] == True:
        window[("ffxiv_hyur", 'style')].update(disabled=False)
        window[("ffxiv_lala", 'style')].update(disabled=False)
        window[("ffxiv_miqote",'style')].update(disabled=False)
        window[("ffxiv_aura",'style')].update(disabled=False)
        pass
    else:
        window[("ffxiv_hyur", 'style')].update(disabled= True)
#        window[("ffxiv_hyur", 'style')].update(value= False)
        window[("ffxiv_lala", 'style')].update(disabled= True)
#        window[("ffxiv_lala", 'style')].update(value= False)
        window[("ffxiv_miqote",'style')].update(disabled=True)
#        window[("ffxiv_miqote", 'style')].update(value= False)
        window[("ffxiv_aura",'style')].update(disabled=True)
        pass

    if values[('character_restrictions', 'restrictions')] == True:
        window[('character_objectives', 'restrictions')].update(disabled=False)
        window[('character_esc_clause', 'restrictions')].update(disabled=False)
        pass
    else:
        window[("character_objectives", 'restrictions')].update(disabled=True)
        window[("character_esc_clause", 'restrictions')].update(disabled=True)
        pass
    if values['character_class'] == True:
        window['character_class_combo'].update(disabled=False)
        pass
    else:
        window['character_class_combo'].update(disabled=True)


    if event == 'generate':
        l = []
        x = values.values()
        y = values.keys()
        for i in range(len(x)):
            if list(x)[i] == True:
                l.append(list(y)[i])

        style = [item for item in l if item[1] == 'style']
        if len(style) == 2 and style[0][0] != 'simple':
            style = style.pop(1)[0]
        elif len(style) == 2 and style[0][0] == 'simple':
            style = 'simple'
        elif 'ffxiv' in l:
            style = [item for item in l if item[1] == 'style'][0][0]

        sex   = [item for item in l if item[1] == 'sex'][0][0]

        if 'firstname' in l:
            firstname = names.generate_firstname(sex=sex,style=style)
        else:
            firstname = ""

        if 'surname' in l:
            lastname = names.generate_surname(style=style)
        else:
            lastname = ""

        if 'firstname' in l:
            print(firstname + " " + lastname)
        elif 'firstname' and 'surname' not in l:
            pass
        elif 'firstname' not in l:
            print(lastname)

        #r = [item for item in l if item[1] == 'restrictions']
        #if r:
        #    if r[0][0] == 'character_restrictions':
        #        character_restriction = restrictions.generate_restrictions(r[0][0])
        #        print(character_restriction)

        if 'character_backstory' in l:
            lore = backstory.generate_background()
            print(lore)

        if 'character_class' in l:
            game = values['character_class_combo']
            char_class = character_class.generate_class(game=game)
            print(char_class)

        pass
    if event == 'cancel':
        window.close()

window.close()


## kind of unnecessary when there is no generation-name or fitness randomization
#class Character:
#    def __init__(self, sex='male', first_name='John', surname='Doe', backstory=backstory.character_background()):
#        self._name = name
#        self._surname = surname
#        self._sex = sex
#        self._backstory = backstory
#
#class Restrictions:
#    def __init__(self):
#        self._osaat = None
#        self._skiller = None
#        self._f2p = None
#        self._ironman = None
#        self._hardcore_ironman = None
#
#class Goals:
#    def __init__(self):
#        self._gather = None
#        self._combat = None
#        self._crafting = None
#        self._completionist = None
