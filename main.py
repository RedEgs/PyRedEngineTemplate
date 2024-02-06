
import pygame, json, os, sys

import pyredengine 
from pyredengine import SceneService

import scenes.example_scene as example_scene
class Main(pyredengine.App):
    def __init__(self):
        super().__init__()
    
    def load_scenes(self):
        self.scenes.load_scenes([example_scene.Example_Scene("example_scene", self)])
        self.scenes.set_scene("example_scene")  
         

        
if __name__ == "__main__":
    main = Main()
    main.run()
