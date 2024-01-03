import os
import names
import backstory
import restrictions
import character_class
import PySimpleGUI as sg

sg.set_options(text_justification='right')

sg.theme('Dark')
layout = [
          #[sg.Text('Simple character generator')],
          [sg.Text('Simple character generator', font=('Helvetica', 15))],
          #[sg.Text(' ', font=('Helvetica', 15))],
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
               sg.Combo(values=['Unspecified game', 'Black Desert', 'FFXIV', 'World of Warcraft' ], default_value=['Unspecified game'], disabled=True, enable_events=True, key='character_class_combo', readonly=True),\
               sg.Checkbox('Genderlock class choice', default=True, key='character_class_genderlock', visible=False)],
          [sg.Text(' ' * 100, size=(65,1))],
          #[sg.Text('_' * 100, size=(65,1))],
          #[sg.Output(size=(62,10), echo_stdout_stderr=True, key='output')],
          #[sg.Text('_' * 100, size=(65,1))],
          #[sg.Text('Generate', size=(8, 1)), sg.Spin(values=[i for i in range(1, 21)], key='generate_amount', initial_value=1, size=(4, 1)), sg.Text('character(s).')],
          #[sg.Button('Generate', enable_events=True, key='generate'), sg.Cancel(key='cancel')]
         ]

tab_1 = layout

tab_2 = [
         [sg.Text(' ', font=('Helvetica', 15))],
         [sg.Text('Only available with Simple naming convention')],
         #[sg.Text(' ', font=('Helvetica', 15))],
         [sg.Checkbox('Firstname', disabled=False, enable_events=True, k=('man_firstname','advanced_options')), \
             sg.Push(),
             sg.Text('Begins with: '),sg.InputText(size=(10,1), disabled=False, enable_events=True, k=('firstname_beginning_input','advanced_options')), \
             sg.Text('Ends with: '),  sg.InputText(size=(10,1), disabled=False, enable_events=True, k=('firstname_ending_input','advanced_options'))],
         [sg.Checkbox('Surname', disabled=False, enable_events=True, k=('man_surname','advanced_options')),\
             sg.Push(),
             sg.Text('Begins with: '), sg.InputText(size=(10,1), disabled=False, enable_events=True, k=('surname_beginning_input','advanced_options')), \
             sg.Text('Ends with: '),   sg.InputText(size=(10,1), disabled=False, enable_events=True, k=('surname_ending_input','advanced_options'))]
        ]

all_layout =  [
               [sg.TabGroup([[sg.Tab('Main', tab_1), sg.Tab('Advanced name options', tab_2)]])],
               [sg.Text('Generate', size=(8, 1)), sg.Spin(values=[i for i in range(1, 21)], key='generate_amount', initial_value=1, size=(4, 1)), sg.Text('character(s).')],
               [sg.Output(size=(43,10), echo_stdout_stderr=True, key='output', font=('Helvetica', 15))],
               [sg.Button('Generate', enable_events=True, key='generate', bind_return_key=True, focus=True), sg.Cancel(key='cancel')]
              ]

window = sg.Window('character generator', all_layout, finalize=True)
window['generate'].set_focus()


def canvas():
    while True:
        event, values = window.read()

        if values[('man_firstname','advanced_options')] == False:
            window[('firstname_beginning_input','advanced_options')].update('')
            window[('firstname_ending_input','advanced_options')].update('')

        if values[('man_surname','advanced_options')] == False:
            window[('surname_beginning_input','advanced_options')].update('')
            window[('surname_ending_input','advanced_options')].update('')

        if values[('man_firstname','advanced_options')] == True or values[('man_surname','advanced_options')] == True:
            window[('simple','style')].update(True)
            window[('realistic','style')].update(disabled=True)
            window['ffxiv'].update(disabled=True)
            window[('nickname','style')].update(disabled=True)
        else:
            window[('realistic','style')].update(disabled=False)
            window['ffxiv'].update(disabled=False)
            window[('nickname','style')].update(disabled=False)

        if values['ffxiv'] == True:
            window[("ffxiv_hyur", 'style')].update(disabled=False)
            window[("ffxiv_lala", 'style')].update(disabled=False)
            window[("ffxiv_miqote",'style')].update(disabled=False)
            window[("ffxiv_aura",'style')].update(disabled=False)
        else:
            window[("ffxiv_hyur", 'style')].update(disabled= True)
            window[("ffxiv_lala", 'style')].update(disabled= True)
            window[("ffxiv_miqote",'style')].update(disabled=True)
            window[("ffxiv_aura",'style')].update(disabled=True)

        rerolls = 0
        if values[('character_restrictions', 'restrictions')] == True:
            window[('character_objectives', 'restrictions')].update(disabled=False)
            window[('character_esc_clause', 'restrictions')].update(disabled=False)
            rerolls += 1

            if values[("character_objectives", 'restrictions')] == True:
                rerolls += 1
            if values[("character_esc_clause", 'restrictions')] == True:
                rerolls += 1
        else:
            window[("character_objectives", 'restrictions')].update(disabled=True)
            window[("character_esc_clause", 'restrictions')].update(disabled=True)
            rerolls = 0

        if values['character_class'] == True:
            window['character_class_combo'].update(disabled=False)
        else:
            window['character_class_combo'].update(disabled=True)

        if values['character_class'] == True and values['character_class_combo'] == 'Black Desert':
            window['character_class_genderlock'].update(visible=True)
        else:
            window['character_class_genderlock'].update(visible=False)

        if event == 'generate':
            window['output'].update('')
            activated_options = []
            x = values.values()
            y = values.keys()
            for i in range(len(x)):
                if list(x)[i] == True:
                    activated_options.append(list(y)[i])

            style = [item for item in activated_options if item[1] == 'style']
            if len(style) == 2 and style[0][0] != 'simple':
                style = style.pop(1)[0]
            elif len(style) == 2 and style[0][0] == 'simple':
                style = 'simple'
            elif 'ffxiv' in activated_options:
                style = [item for item in activated_options if item[1] == 'style'][0][0]

            sex   = [item for item in activated_options if item[1] == 'sex'][0][0]

            try:
                generate_amount = int(values['generate_amount'])
            except ValueError:
                print('Enter valid number')
                generate_amount = None

            if generate_amount:
                for i in range(generate_amount):
                    firstname = names.generate_firstname(ending=values[('firstname_ending_input','advanced_options')], beginning=values[('firstname_beginning_input','advanced_options')], sex=sex, style=style)
                    lastname = names.generate_surname(beginning=values[('surname_beginning_input','advanced_options')], ending=values[('surname_ending_input','advanced_options')], style=style, sex=sex)
                    if 'firstname' in activated_options:
                        print(firstname[0], end=' ')
                    if 'surname' in activated_options:
                        print(lastname[0])

            if values[('character_restrictions', 'restrictions')]:
                print('Restriction: ' + restrictions.generate_restriction())

                if values[('character_objectives', 'restrictions')]:
                    print('Goal: ' + restrictions.generate_goals())

                if values[('character_esc_clause','restrictions')]:
                    print('Escape clause: ' + restrictions.generate_esc_clause())

            if 'character_backstory' in activated_options:
                lore = backstory.generate_background()
                print('Background: ' + lore)

            if 'character_class' in activated_options:
                game = values['character_class_combo']
                char_class = character_class.generate_class(game=game, sex=sex, genderlock=values['character_class_genderlock'])
                print('Class: ' + char_class)

        if event == 'cancel':
            window.close()
