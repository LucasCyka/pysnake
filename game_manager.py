"""
Control all the game states
"""

from state import State
import pygame as py
import sys

glb = None #global singleton
screen = None
currentState = State.MENU
stateObj = None

def init(glbs,scr): 
    global glb
    global screen

    glb = glbs
    screen = scr


    main()  

def main():
    global currentState


    while currentState != State.EXITING:
        #main game loop

        screen.fill(py.color.Color(0,0,0))
        py.display.flip()
        

        for event in py.event.get():
            if event.type == py.QUIT:
                currentState = State.EXITING
        
    
def update_state():
    match currentState:
        case State.MENU:
            pass

    pass


def load_menu():
    pass