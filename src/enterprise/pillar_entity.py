from typing import List

from src.enterprise.value_objects import Vector
from src.renderer import Renderer
from src.enterprise.value_objects import Color
from src.events import Events
from src.enterprise.game_object_entity import GameObjectEntity

from src.settings import Settings

class PillarEntity(GameObjectEntity):

    def __init__(self, id : int, position: Vector, color: Color = Color(255,255,255)):
        super().__init__(id)
        self.tamanho = 0.2 # metros
        self.position = position
        self.color = color
        self.ligacoes: List[PillarEntity] = []
        self.selected = False
    
    def is_over(self, position: Vector) -> None:
        tamanho_pixels = self.tamanho * Settings.PIXELS_POR_METRO
        x_ini = self.position.x - tamanho_pixels / 2
        x_fim = self.position.x + tamanho_pixels / 2
        y_ini = self.position.y - tamanho_pixels / 2
        y_fim = self.position.y + tamanho_pixels / 2
        if x_ini < position.x < x_fim and y_ini < position.y < y_fim:
            return True
    
    def set_selected(self, on: bool) -> None:
        self.selected = on

    def update(self):
        if self.selected:
            new_x = Events.MOUSE_POS.x // 3.5
            new_y = Events.MOUSE_POS.y // 3.5
            self.position = Vector(new_x * 3.5, new_y * 3.5)

    # def render(self):
    #     tamanho_pixels = self.tamanho * Configuracao.PIXELS_POR_METRO
    #     Renderer.quad(self.color, self.posicao, tamanho_pixels)

    #     posicao_metros = Vector(
    #         self.posicao.x / Configuracao.PIXELS_POR_METRO,
    #         self.posicao.y / Configuracao.PIXELS_POR_METRO
    #     )
    #     coord_x, coord_y = posicao_metros.toStr()
    #     Renderer.text(coord_x, self.posicao + Vector(len(coord_x) * 3.5,15), 15)
    #     Renderer.text(coord_y, self.posicao + Vector(len(coord_y) * 3.5,30), 15)