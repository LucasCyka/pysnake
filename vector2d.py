"""
Simple Vector 2D class
"""

class Vector2D():

    def __init__(self,x,y) -> None:

        self.x=x
        self.y=y
        pass

    def __add__(v1,v2):
        return Vector2D(v1.x+v2.y,v1.y+v2.y)