"""
Define singletons and check for errors.
"""

import globals
import game_manager
import pygame as py

def main():
    #TODO MIXER AND FONTS ERRORS HERE
    glb = globals.Globals()
    glb.screenSize = 800,600

    py.init()
    if py.display.get_driver() == "Windows":
        try:
            screen = py.display.set_mode(glb.screenSize,py.OPENGL)
            py.display.set_caption("SNAKE")
        except:
            return
    else:         
        try:
            screen = py.display.set_mode(glb.screenSize,py.FULLSCREEN)
        except:
            print("Error graphics initializing driver.")
            return
    py.display.set_caption("SNAKE")
    game_manager.init(glb,screen)
