from src.enterprise.terrain_entity import TerrainEntity
from src.enterprise.screen_entity import ScreenEntity
from src.enterprise.value_objects import Vector, Color
from src.application.renders import IScreenRender

class RenderTerrainUseCase:

    def __init__(self, screen_render: IScreenRender):
        self.screen_render = screen_render

    def execute(self, terrain_entity: TerrainEntity):
        largura_pixels = terrain_entity.largura * terrain_entity.pixel_por_metro
        comprimento_pixels = terrain_entity.comprimento * terrain_entity.pixel_por_metro

        p1 = Vector(0,0)
        p2 = Vector(comprimento_pixels,0)

        for i in range(terrain_entity.largura + 1):
            self.screen_render.line(p1, p2, Color(35,35,35))
            p1 += Vector(0, terrain_entity.pixel_por_metro)
            p2 += Vector(0, terrain_entity.pixel_por_metro)
        
        p1 = Vector(0,0)
        p2 = Vector(0,largura_pixels)

        for i in range(terrain_entity.comprimento + 1):
            self.screen_render.line(p1, p2, Color(35,35,35))
            p1 += Vector(terrain_entity.pixel_por_metro, 0)
            p2 += Vector(terrain_entity.pixel_por_metro, 0)