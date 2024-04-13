"""
Define singletons and check for errors.
"""

import globals
import game_manager
import pygame as py

def main():
    #TODO MIXER AND FONTS ERRORS HERE
    glb = globals.Globals()
    glb.size = 800,600

    py.init()
    print(py.display.get_driver())
    try:
        screen = py.display.set_mode(glb.size,py.OPENGL)
        py.display.set_caption("SNAKE")
    except:
        print("Error initializing screen")
    game_manager.init(glb,screen)
