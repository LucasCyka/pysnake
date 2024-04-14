"""
main menu state logic
"""
import pygame as py
import pygame.freetype
from state import State
import os

screen = None
glbs = None

buttons = {
    0:{"Text":"Start","size":20},
    1:{"Text":"Options","size":20},
    2:{"Text":"About","size":20},
    3:{"Text":"Quit","size":20}
}

class TextButton():
    
    def __init__(self) -> None:
        self.font =  pygame.freetype.Font(os.path.join(glbs.assetsDir,"fonts/DejaVuSerif-Bold.ttf"),20)
        self.selected = False

class Menu():

    btn1Text = "START"

    def __init__(self,scr,globals):
        global screen
        global glbs

        screen = scr
        glbs = globals

        self.btn1 = TextButton()

        for btn in buttons:
            print(buttons[btn]["Text"])

    

    #menu logic
    #return any change to this state
    def update(self) -> State:
        
        _btn1_size = self.btn1.font.get_rect(Menu.btn1Text).size

        self.btn1.font.render_to(screen,(glbs.screenSize[0]/2-(_btn1_size[0]/2),glbs.screenSize[1]/2-(_btn1_size[1]/2)),Menu.btn1Text,(255,255,255))
       

        return State.MENU