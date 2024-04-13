"""
Main singleton
"""

class Globals:

    _instance = None
    screenSize = 0,0

    def __new__(cls):
        if cls._instance == None:
            Globals._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self,"initialized"):
            self.initialized = True

        return