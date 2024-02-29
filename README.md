# Character Generator

a program to quickly generate character name with additional options such as backstory, playthrough-limitations or trivial goals

## To-do

- code refactor
  - let name generation output first+surnames regardless of options
- code tests
- name constraints (i.e length, spaces)
- add tolkien/historic/roman/greek/korean/japanese/chinese/nordic style names
- re-design GUI
- install script/binaries
- pylint

## Features

- name generation
  - firstname/surname
    - Sex
    - choose beginning/endings
    - style
      - Simple
      - FFXIV
      - Nickname
      - Realistic
- playthrough-limitations
  - Realistic
  - character lore
  - escape clause
  - class
    - based on game

### Proposed features

- Sex
- Name
    - generate names like X (or wildly different, slider-option)
      - menu-right click option
    - alternate name generation method (markov chain,  procedural, ai)
    - common constraints
        - length
        - style
- Backstory
    - dreams/hopes 
    - likes/dislikes
- Difficulty setting 
    - re-roll character/restriction/goal only
      - X amount of re-rolls

#### name generation
- pre-determined beginnings and endings
- markov chain
- generate similar name (based on input)
 

#### AI
- use tags to feed into chat GPT to provide a character background
- use tags to feed into stable diffufsion
    - image creation based on generated character

## Screenshots

![picture](https://github.com/haaln/char-gen/blob/master/screenshot/screenshot.png?raw=true)
