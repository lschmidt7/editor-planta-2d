import pygame

from src.enterprise.value_objects import Color, Vector

from src.application.renders import IRender

class Render(IRender):

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
    
    def quad(self, position: Vector, size: int, color: Color) -> None:
        top = int(position.x - size / 2)
        left = int(position.y - size / 2)
        pygame.draw.rect(self.screen, color.tupple(), (top, left, size, size))