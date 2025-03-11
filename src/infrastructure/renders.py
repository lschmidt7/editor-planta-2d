import pygame

from src.enterprise.pillar_entity import PillarEntity
from src.enterprise.wall_entity import WallEntity
from src.enterprise.value_objects import Color, Vector

from src.application.renders import IPillarRender, IWallRender, IScreenRender

class ScreenRender(IScreenRender):

    def initialize(self, width: int, height: int, title: str):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
    
    def update(self):
        pygame.display.update()

    def render(self):
        self.screen.fill(Color(0,0,0).tupple())
    
    def line(self, start: Vector, end: Vector, color: Color):
        pygame.draw.line(self.screen, color.tupple(), start.tupple(), end.tupple())

class PillarRender(IPillarRender):

    def __init__(self):
        pass
    
    def render(self, pillar: PillarEntity):
        pass

class WallRender(IWallRender):

    def __init__(self):
        pass
    
    def render(self, wall: WallEntity):
        pass