from src.enterprise.terrain_entity import TerrainEntity
from src.enterprise.value_objects import Vector, Color
from src.application.renders import IRender
from src.settings import Settings

class CreateTerrainUseCase:

    def __init__(self):
        pass

    def execute(self, largura: int, comprimento: int) -> TerrainEntity:
        terrain_entity = TerrainEntity(largura, comprimento)
        return terrain_entity

class RenderTerrainUseCase:

    def __init__(self, screen_render: IRender):
        self.screen_render = screen_render

    def execute(self, terrain_entity: TerrainEntity, color: Color):
        largura_pixels = terrain_entity.largura * Settings.PIXELS_POR_METRO
        comprimento_pixels = terrain_entity.comprimento * Settings.PIXELS_POR_METRO

        p1 = Vector(0,0)
        p2 = Vector(comprimento_pixels,0)

        for i in range(terrain_entity.largura + 1):
            self.screen_render.line(p1, p2, color)
            p1 += Vector(0, Settings.PIXELS_POR_METRO)
            p2 += Vector(0, Settings.PIXELS_POR_METRO)
        
        p1 = Vector(0,0)
        p2 = Vector(0,largura_pixels)

        for i in range(terrain_entity.comprimento + 1):
            self.screen_render.line(p1, p2, color)
            p1 += Vector(Settings.PIXELS_POR_METRO, 0)
            p2 += Vector(Settings.PIXELS_POR_METRO, 0)