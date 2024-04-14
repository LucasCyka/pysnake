"""
Control all the game states
"""

from state import State
import pygame as py
import sys
import menu

glbs = None #global singleton
screen = None
currentState = State.MENU
stateObj = None


def init(glb,scr): 
    global glbs
    global screen

    glbs = glb
    screen = scr

    change_state()
    main()  

def main():
    global currentState


    while currentState != State.EXITING:
        #main game loop

        screen.fill(py.color.Color(0,0,0))
        _newState = stateObj.update()
        py.display.flip()

        if _newState != currentState: 
            currentState = _newState
            change_state()

        for event in py.event.get():
            if event.type == py.QUIT:
                currentState = State.EXITING
                change_state()
        
    
def change_state():
    global stateObj

    match currentState:
        case State.MENU:
            stateObj = menu.Menu(screen,glbs)
        case State.EXITING:
            pass

    pass


def load_menu():
    pass