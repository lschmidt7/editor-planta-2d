from pygame.draw import line, rect, circle
from pygame import Rect, font

from src.enterprise.value_objects import Color, Vector

class Renderer:

    surface = None

    def line(color: Color, start: Vector, end: Vector, width: int):
        line(Renderer.surface, color.tupple(), start.tupple(), end.tupple(), width)
    
    def quad(color: Color, position: Vector, size: int):
        left = position.x - size / 2
        top = position.y - size / 2
        rect(Renderer.surface, color.tupple(), Rect(left, top, size, size))
    
    def circle(color: Color, position: Vector, radius: int):
        circle(Renderer.surface, color.tupple(), position.tupple(), radius)
    
    def text(text: str, position : Vector, size: int = 20) -> None:
        fonte = font.Font(None, size)
        surface = fonte.render(text, True, (150,150,150))
        rect = surface.get_rect(center=position.tupple())
        Renderer.surface.blit(surface, rect)