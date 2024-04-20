"""
main menu state logic
"""
import pygame as py
import pygame.freetype
from state import State
from vector2d import Vector2D
import os


screen = None
glbs = None

buttons = {
    0:{"text":"START","size":20,"obj":None},
    1:{"text":"OPTIONS","size":20,"obj":None},
    2:{"text":"ABOUT","size":20,"obj":None},
    3:{"text":"QUIT","size":20,"obj":None}
}

class TextButton():
    
    def __init__(self,size) -> None:
        self.font =  pygame.freetype.Font(os.path.join(glbs.assetsDir,"fonts/DejaVuSerif-Bold.ttf"),size)
        self.selected = False

class img():
    pass

class Menu():

    _btn_spacing = 50

    def __init__(self,scr,globals):
        global screen
        global glbs

        screen = scr
        glbs = globals

        self.btn1 = TextButton(20)

        for btn in buttons:
            buttons[btn]["obj"] = TextButton(buttons[btn]["size"])
 

    #menu logic
    #return any change to this state
    def update(self) -> State:
        initial_btn_y = glbs.screenSize[1]/len(buttons.keys())
        _spacing = 0
        
        for btn in buttons:
            _obj = buttons[btn]["obj"]
            _txt = buttons[btn]["text"]
            btn_size = _obj.font.get_rect(_txt).size

            _scr_pos = Vector2D(glbs.screenSize[0],glbs.screenSize[1])
            _scr_pos.x = _scr_pos.x/2-btn_size[0]/2
            _scr_pos.y = initial_btn_y+btn_size[1]+_spacing

            _obj.font.render_to(screen,(_scr_pos.x,_scr_pos.y),_txt,(255,255,255))
            
            _spacing+=Menu._btn_spacing

        #_btn1_size = self.btn1.font.get_rect(Menu.btn1Text).size

        #self.btn1.font.render_to(screen,(glbs.screenSize[0]/2-(_btn1_size[0]/2),glbs.screenSize[1]/2-(_btn1_size[1]/2)),Menu.btn1Text,(255,255,255))
       

        return State.MENU