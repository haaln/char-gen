#!/usr/bin/env python3

import os
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
#         [sg.Checkbox('Enable advanced settings', enable_events=True, default=False, key='advanced_checkbox')],
#         [sg.Checkbox('Length constraint', key=('length_constraint','advanced_options'), enable_events=True, disabled=True), \
#             sg.Spin(values=[i for i in range(1,16)], initial_value=9, size=(4,1), key=('length_spinner','advanced_options'), enable_events=True, disabled=True)],
#         [sg.Checkbox('Exclude characters',key=('exclude_char_checkbox','advanced_options'), enable_events=True, disabled=True), \
#             sg.InputText(size=(10,1),key=('exclude_char_input','advanced_options'), enable_events=True, disabled=True)],
#         [sg.Checkbox('Include characters',key=('include_char_checkbox','advanced_options'), enable_events=True, disabled=True), \
#             sg.InputText(size=(10,1), key=('include_char_input','advanced_options'), enable_events=True, disabled=True)],
#         [sg.Checkbox('Allow spaces', key=('allow_spaces','advanced_options'), enable_events=True, disabled=True), \
#             sg.Checkbox('Replace spaces with underscores', key=('replace_underscore','advanced_options'), enable_events=True, disabled=True)],
#         [sg.Checkbox('Begins with: ', enable_events=True, k=('begins_with','advanced_options')), \
#             sg.InputText(size=(10,1), enable_events=True, k=('begins_with_input','advanced_options')), \
#             sg.Checkbox('Ends with: ', enable_events=True, k=('ends_with','advanced_options')), \
#             sg.InputText(size=(10,1), enable_events=True, k=('ends_with_input','advanced_options'))],
#         [sg.Radio('Manually choose name', 4, enable_events=True, k=('manual_name','advanced_options'))],
#         [sg.Checkbox('First name: ', enable_events=True, k=('man_firstname','advanced_options')), \
#             sg.InputText(size=(10,1), enable_events=True, k=('man_firstname_input','advanced_options')), \
#             sg.Checkbox('Surname: ', enable_events=True, k=('man_surname','advanced_options')), \
#             sg.InputText(size=(10,1), enable_events=True, k=('man_surname_input','advanced_options'))],
#         [sg.Radio('generate similar to: ', 2, enable_events=True, k=('similar_to','advanced_options')), \
#             sg.Text('First name: ', enable_events=True, k=('similar_firstname','advanced_options')), \
#             sg.InputText(size=(10,1), enable_events=True, k=('similar_firstname_input','advanced_options')), \
#             sg.Text('Last name: ', enable_events=True, k=('similar_surname','advanced_options')), \
#             sg.InputText(size=(10,1), enable_events=True, k=('similar_surname_input','advanced_options'))],
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
#        [sg.Radio('Japanese', 2, key=('japanese', 'style'), enable_events=True)],
#         [sg.Radio('Korean', 2)],
#         [sg.Radio('Chinese', 2)],
          [sg.Text('_' * 100, size=(65,1))],
          [sg.Text('Additional features', font=('Helvetica', 15))],
          [sg.Checkbox('Character restrictions', key=('character_restrictions', 'restrictions'), enable_events=True, tooltip=' Generate a character restriction such as Ironman mode '), \
               sg.Checkbox('Objectives', tooltip=' Provides a random goal to achieve with this character ', key=('character_objectives', 'restrictions'), disabled=True), \
               sg.Checkbox('Escape clause', tooltip=' Allow a condition where if fulfilled, you may forego your character restriction ', key=('character_esc_clause', 'restrictions'), disabled=True)],
          [sg.Checkbox('Character background', tooltip=' Generates random trivia ', key='character_backstory')],
          [sg.Checkbox('Character class', key='character_class', enable_events=True, tooltip=' Picks a random class for the character depending on game '), \
               sg.Combo(values=['Black Desert', 'FFXIV', 'World of Warcraft', 'Unspecified'], default_value=['Unspecified'], disabled=True, enable_events=True, key='character_class_combo', readonly=True),\
               sg.Checkbox('Genderlock class choice', default=True, key='character_class_genderlock', visible=False)],
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
        window[("ffxiv_lala", 'style')].update(disabled= True)
        window[("ffxiv_miqote",'style')].update(disabled=True)
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

    if values['character_class'] == True and values['character_class_combo'] == 'Black Desert':
        window['character_class_genderlock'].update(visible=True)
    else:
        window['character_class_genderlock'].update(visible=False)


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
            os.system('cls' if os.name == 'nt' else 'clear')
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

        r = [item[0] for item in l if item[1] == 'restrictions']
        if r:
            if r[0] == 'character_restrictions':
                character_restriction = restrictions.generate_restrictions(restrict=values[('character_restrictions','restrictions')],goals=values[('character_objectives','restrictions')],escape=values[('character_esc_clause','restrictions')])
                print(character_restriction)

        if 'character_backstory' in l:
            lore = backstory.generate_background()
            print(lore)

        if 'character_class' in l:
            game = values['character_class_combo']
            char_class = character_class.generate_class(game=game, sex=sex, genderlock=values['character_class_genderlock'])
            print(char_class)

        pass
    if event == 'cancel':
        window.close()

window.close()

#   if values['advanced_checkbox'] == True:
#       window[('similar_to','advanced_options')].update(visible=True)
#       window[('similar_to','advanced_options')].update(disabled=False)
#       window[('length_constraint','advanced_options')].update(visible=True)
#       window[('length_constraint','advanced_options')].update(disabled=False)
#       window[('length_spinner','advanced_options')].update(visible=True)
#       window[('length_spinner','advanced_options')].update(disabled=False)
#       window[('exclude_char_checkbox','advanced_options')].update(visible=True)
#       window[('exclude_char_checkbox','advanced_options')].update(disabled=False)
#       window[('exclude_char_input','advanced_options')].update(visible=True)
#       window[('exclude_char_input','advanced_options')].update(disabled=False)
#       window[('allow_spaces','advanced_options')].update(visible=True)
#       window[('allow_spaces','advanced_options')].update(disabled=False)
#       window[('replace_underscore','advanced_options')].update(visible=True)
#       window[('replace_underscore','advanced_options')].update(visible=True)
#       window[('begins_with','advanced_options')].update(visible=True)
#       window[('begins_with','advanced_options')].update(disabled=False)
#       window[('begins_with_input','advanced_options')].update(visible=True)
#       window[('begins_with_input','advanced_options')].update(disabled=False)
#       window[('ends_with','advanced_options')].update(visible=True)
#       window[('ends_with','advanced_options')].update(disabled=False)
#       window[('ends_with_input','advanced_options')].update(visible=True)
#       window[('ends_with_input','advanced_options')].update(disabled=False)
#       window[('include_char_checkbox','advanced_options')].update(visible=True)
#       window[('include_char_checkbox','advanced_options')].update(disabled=False)
#       window[('include_char_input','advanced_options')].update(visible=True)
#       window[('include_char_input','advanced_options')].update(disabled=False)
#       window[('manual_name','advanced_options')].update(visible=True)
#       window[('manual_name','advanced_options')].update(disabled=False)
#       window[('man_firstname','advanced_options')].update(visible=True)
#       window[('man_firstname','advanced_options')].update(disabled=False)
#       window[('man_firstname_input','advanced_options')].update(visible=True)
#       window[('man_firstname_input','advanced_options')].update(disabled=False)
#       window[('man_surname','advanced_options')].update(visible=True)
#       window[('man_surname','advanced_options')].update(disabled=False)
#       window[('man_surname_input','advanced_options')].update(visible=True)
#       window[('man_surname_input','advanced_options')].update(disabled=False)
#       window[('similar_firstname','advanced_options')].update(visible=True)
#       #window[('similar_firstname','advanced_options')].update(disabled=False)
#       window[('similar_firstname_input','advanced_options')].update(visible=True)
#       window[('similar_firstname_input','advanced_options')].update(disabled=False)
#       window[('similar_surname','advanced_options')].update(visible=True)
#       #window[('similar_surname','advanced_options')].update(disabled=False)
#       window[('similar_surname_input','advanced_options')].update(visible=True)
#       window[('similar_surname_input','advanced_options')].update(disabled=False)
#   else:
#       window[('similar_to','advanced_options')].update(visible=False)
#       window[('similar_to','advanced_options')].update(disabled=True)
#       window[('similar_to','advanced_options')].update(False)

#       window[('include_char_checkbox','advanced_options')].update(visible=False)
#       window[('include_char_checkbox','advanced_options')].update(disabled=True)
#       window[('include_char_input','advanced_options')].update(visible=False)
#       window[('include_char_input','advanced_options')].update(disabled=True)
#       window[('length_constraint','advanced_options')].update(visible=False)
#       window[('length_constraint','advanced_options')].update(disabled=True)
#       window[('length_spinner','advanced_options')].update(visible=False)
#       window[('length_spinner','advanced_options')].update(disabled=True)
#       window[('exclude_char_checkbox','advanced_options')].update(visible=False)
#       window[('exclude_char_checkbox','advanced_options')].update(disabled=True)
#       window[('exclude_char_input','advanced_options')].update(visible=False)
#       window[('exclude_char_input','advanced_options')].update(disabled=True)
#       window[('allow_spaces','advanced_options')].update(visible=False)
#       window[('allow_spaces','advanced_options')].update(disabled=True)
#       window[('replace_underscore','advanced_options')].update(disabled=True)
#       window[('replace_underscore','advanced_options')].update(visible=False)
#       window[('begins_with','advanced_options')].update(disabled=True)
#       window[('begins_with','advanced_options')].update(visible=False)
#       window[('begins_with_input','advanced_options')].update(disabled=True)
#       window[('begins_with_input','advanced_options')].update(visible=False)
#       window[('ends_with','advanced_options')].update(disabled=True)
#       window[('ends_with','advanced_options')].update(visible=False)
#       window[('ends_with_input','advanced_options')].update(disabled=True)
#       window[('ends_with_input','advanced_options')].update(visible=False)
#       window[('manual_name','advanced_options')].update(disabled=True)
#       window[('manual_name','advanced_options')].update(visible=False)
#       window[('man_firstname','advanced_options')].update(disabled=True)
#       window[('man_firstname','advanced_options')].update(visible=False)
#       window[('man_firstname_input','advanced_options')].update(disabled=True)
#       window[('man_firstname_input','advanced_options')].update(visible=False)
#       window[('man_surname','advanced_options')].update(disabled=True)
#       window[('man_surname','advanced_options')].update(visible=False)
#       window[('man_surname_input','advanced_options')].update(disabled=True)
#       window[('man_surname_input','advanced_options')].update(visible=False)
#       #window[('similar_firstname','advanced_options')].update(disabled=True)
#       window[('similar_firstname','advanced_options')].update(visible=False)
#       window[('similar_firstname_input','advanced_options')].update(disabled=True)
#       window[('similar_firstname_input','advanced_options')].update(visible=False)
#       #window[('similar_surname','advanced_options')].update(disabled=True)
#       window[('similar_surname','advanced_options')].update(visible=False)
#       window[('similar_surname_input','advanced_options')].update(disabled=True)
#       window[('similar_surname_input','advanced_options')].update(visible=False)

#   if values[('begins_with','advanced_options')] == True or values[('ends_with','advanced_options')] == True:
#       window[('simple','style')].update(True)
#       window[('realistic','style')].update(disabled=True)
#       window['ffxiv'].update(disabled=True)
#       window[('nickname','style')].update(disabled=True)
#   else:
#       window[('realistic','style')].update(disabled=False)
#       window['ffxiv'].update(disabled=False)
#       window[('nickname','style')].update(disabled=False)

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
