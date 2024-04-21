"""
Generic graphic user interface.
Draw things like buttons, labels e images on a surface.
"""

import pygame as py
import os

#gui element base class
class Gui():

    surface = None
    glbs = None

    def __init__(self,srfc,sel,globals):
        Gui.surface = srfc
        Gui.glbs = globals
        self.selectable = sel
        
        if self.selectable: self.selected = False
        

class Image(py.sprite.Sprite,Gui):

    def __init__(self,img):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(os.path.join(Gui.glbs.assetsDir+"/imgs",img))
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.topleft = (0,350)

    def drawImage(self):
        py.sprite.Group(self).draw(Gui.surface)
        pass

class TextButton(Gui):
    
    def __init__(self,size) -> None:
        self.font =  py.freetype.Font(os.path.join(Gui.glbs.assetsDir,"fonts/DejaVuSerif-Bold.ttf"),size)

class Label(Gui):
    
    def __init__(self):
        print(Gui.surface)

        pass