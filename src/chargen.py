#!/usr/bin/env python3

import os
import names
import backstory
import restrictions
import character_class
import PySimpleGUI as sg

sg.set_options(text_justification='right')

sg.theme('Dark')
layout = [[sg.Text('Simple character generator')],
          [sg.Text('Main', font=('Helvetica', 15))],
          [sg.Checkbox('First name', default=True, key='firstname'), sg.Checkbox('Surname', default=True, key='surname')],
          [sg.Radio('Male', 1, default=True, key=('male', 'sex')), sg.Radio('Female', 1, key=('female', 'sex'))],
          [sg.Text('_' * 100, size=(65,1))],
          [sg.Text('Naming convention', font=('Helvetica', 15))],
          [sg.Radio('Simple', 2, default=True, key=('simple', 'style'), enable_events=True)],
          [sg.Radio('FFXIV', 2, key='ffxiv', enable_events=True),\
               sg.Radio('Hyur', 3, disabled=True, default=True, key=('ffxiv_hyur','style')),\
               sg.Radio('Lalafell', 3, disabled=True, key=('ffxiv_lala','style')),\
               sg.Radio('Au Ra', 3, disabled=True, key=('ffxiv_aura','style')),\
               sg.Radio("Miqo'te", 3, disabled=True, key=('ffxiv_miqote', 'style'))],
          [sg.Radio('Nickname', 2, key=('nickname', 'style'), enable_events=True)],
          [sg.Radio('Realistic', 2, key=('realistic', 'style'), enable_events=True)],
          [sg.Text('_' * 100, size=(65,1))],
          [sg.Text('Additional features', font=('Helvetica', 15))],
          [sg.Checkbox('Character restrictions', key=('character_restrictions', 'restrictions'), enable_events=True, tooltip=' Generate a character restriction such as Ironman mode '), \
               sg.Checkbox('Objectives', tooltip=' Provides a random goal to achieve with this character ', key=('character_objectives', 'restrictions'), disabled=True), \
               sg.Checkbox('Escape clause', tooltip=' Allow a condition where if fulfilled, you may forego your character restriction ', key=('character_esc_clause', 'restrictions'), disabled=True)],
          [sg.Checkbox('Character background', tooltip=' Generates random trivia ', key='character_backstory')],
          [sg.Checkbox('Character class', key='character_class', enable_events=True, tooltip=' Picks a random class for the character depending on game '), \
               sg.Combo(values=['Black Desert', 'FFXIV', 'World of Warcraft', 'Unspecified game'], default_value=['Unspecified game'], disabled=True, enable_events=True, key='character_class_combo', readonly=True),\
               sg.Checkbox('Genderlock class choice', default=True, key='character_class_genderlock', visible=False)],
          [sg.Text('_' * 100, size=(65,1))],
          [sg.Output(size=(62,10), key='-OUTPUT-')],
          [sg.Text('_' * 100, size=(65,1))],
          [sg.Text('Generate', size=(8, 1)), sg.Spin(values=[i for i in range(1, 21)], key='generate_amount', initial_value=1, size=(4, 1)), sg.Text('character(s).')],
          [sg.Button('Generate', enable_events=True, key='generate'), sg.Cancel(key='cancel')] ]

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
        window['-OUTPUT-'].update('')
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

        for i in range(values['generate_amount']):
            if 'firstname' in l:
                os.system('cls' if os.name == 'nt' else 'clear')
                firstname = names.generate_firstname(sex=sex,style=style)
            else:
                firstname = ""

            if 'surname' in l:
                lastname = names.generate_surname(style=style, sex=sex)
            else:
                lastname = ""

            if 'firstname' in l:
                print('Name: ' + firstname + " " + lastname)
            elif 'firstname' and 'surname' not in l:
                pass
            elif 'firstname' not in l:
                print('Name: ' +lastname)

        r = [item[0] for item in l if item[1] == 'restrictions']
        if r:
            if r[0] == 'character_restrictions':
                character_restriction = restrictions.generate_restriction(restrict=values[('character_restrictions','restrictions')])
                print('Restriction: ' + character_restriction)
                character_goal = restrictions.generate_goals(goals=True, restrict=values[('character_objectives','restrictions')])
                if character_goal:
                    print('Goal: ' + character_goal)
                character_esc_clause = restrictions.generate_esc_clause(escape=True, restrict=values[('character_esc_clause','restrictions')])
                if values[('character_esc_clause','restrictions')]:
                    print('Escape clause: ' + character_esc_clause)


        if 'character_backstory' in l:
            lore = backstory.generate_background()
            print('Background: ' +lore)

        if 'character_class' in l:
            game = values['character_class_combo']
            char_class = character_class.generate_class(game=game, sex=sex, genderlock=values['character_class_genderlock'])
            print('Class: ' + char_class)

        pass
    if event == 'cancel':
        window.close()

window.close()

