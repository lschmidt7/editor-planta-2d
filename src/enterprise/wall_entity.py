from src.enterprise.value_objects import Vector, Color
from src.enterprise.pillar_entity import PillarEntity
from src.enterprise.game_object_entity import GameObjectEntity
from src.renderer import Renderer

class WallEntity(GameObjectEntity):
    
    def __init__(self, id : int, posicao_inicio: Vector, posicao_fim: Vector):
        self.id = id
        self.largura = 0.2 # metros
        self.posicao_inicio : Vector = posicao_inicio
        self.posicao_fim : Vector = posicao_fim
        self.inicio : PillarEntity = None
        self.fim : PillarEntity = None
        self.selected : bool = False
    
    def is_over(self, position: Vector) -> None:
        dir = (self.posicao_fim - self.posicao_inicio)
        length = dir.length() / 2
        posicao = self.posicao_inicio + dir.unit() * length
        return posicao.distance(position) < 10
    
    def set_selected(self, on : bool) -> None:
        self.selected = on

    def update(self):
        pass

    def render(self):
        self.posicao_inicio = self.inicio.posicao if self.inicio is not None else self.posicao_inicio
        self.posicao_fim = self.fim.posicao if self.fim is not None else self.posicao_fim
        Renderer.line(Color(255,255,255), self.posicao_inicio, self.posicao_fim, 1)

        distancia = self.posicao_inicio.distance(self.posicao_fim) / Configuracao.PIXELS_POR_METRO
        dir = (self.posicao_fim - self.posicao_inicio)
        length = dir.length() / 2
        posicao = self.posicao_inicio + dir.unit() * length
        Renderer.text(f'{distancia:.2f}m', posicao)