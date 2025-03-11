from src.enterprise.screen_entity import ScreenEntity
from src.enterprise.terrain_entity import TerrainEntity
from src.application.renders import IScreenRender
from src.enterprise.value_objects import Color

class CreateScreenUseCase:

    def __init__(self):
        pass

    def execute(self, terrain_entity: TerrainEntity) -> ScreenEntity:
        width = terrain_entity.comprimento * terrain_entity.pixel_por_metro
        height = terrain_entity.largura * terrain_entity.pixel_por_metro
        screen_entity = ScreenEntity(width, height, Color(0,0,0), 'Planta')
        return screen_entity

class InitScreenUseCase:

    def __init__(self, screen_render: IScreenRender):
        self.screen_render = screen_render
    
    def execute(self, screen_entity: ScreenEntity):
        self.screen_render.initialize(screen_entity.width, screen_entity.height, screen_entity.title)

class DrawScreenUseCase:

    def __init__(self, screen_render: IScreenRender):
        self.screen_render = screen_render
    
    def execute(self):
         self.screen_render.render()

class UpdateScreenUseCase:
     
    def __init__(self, screen_render: IScreenRender):
        self.screen_render = screen_render

    def execute(self):
         self.screen_render.update()