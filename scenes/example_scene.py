import pytweening, pygame, sys, os

import pyredengine
from pyredengine import GuiService
from pyredengine import SceneService


class Example_Scene(SceneService.Scene):
    def __init__(self, scene_name, app):
        super().__init__(scene_name, app)
        
        


    def draw(self):
        self.app.get_screen().fill((255))  
            
        
        
      
