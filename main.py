from src.events import Events

from src.application.usecases.screen_use_cases import (
    CreateScreenUseCase,
    InitScreenUseCase, 
    DrawScreenUseCase, 
    UpdateScreenUseCase
)
from src.application.usecases.scene_use_cases import RenderSceneUseCase
from src.application.usecases.render_terrain_use_case import RenderTerrainUseCase
from src.application.usecases.create_terrain_use_case import CreateTerrainUseCase

from src.enterprise.terrain_entity import TerrainEntity
from src.enterprise.pillar_entity import PillarEntity
from src.enterprise.value_objects import Vector, Color

from src.infrastructure.repositories import PillarRepository, WallRepository
from src.infrastructure.renders import PillarRender, WallRender, ScreenRender

create_terrain_use_case = CreateTerrainUseCase()
terrain_entity = create_terrain_use_case.execute(12, 25, 70)

create_screen_use_case = CreateScreenUseCase()
screen_entity = create_screen_use_case.execute(terrain_entity)

pillar_repository = PillarRepository()
wall_repository = WallRepository()

pillar_render = PillarRender()
wall_render = WallRender()
screen_render = ScreenRender()

render_scene_use_case = RenderSceneUseCase(
    pillar_repository,
    wall_repository,
    pillar_render,
    wall_render
)

init_screen_use_case = InitScreenUseCase(screen_render)
init_screen_use_case.execute(screen_entity)

draw_screen_use_case = DrawScreenUseCase(screen_render)
update_screen_use_case = UpdateScreenUseCase(screen_render)

render_terrain_use_case = RenderTerrainUseCase(screen_render)

pillar_repository.add(PillarEntity(1, Vector(50, 50), Color(255,100,0)))

while not Events.QUIT:
    draw_screen_use_case.execute()

    render_terrain_use_case.execute(terrain_entity)

    render_scene_use_case.execute()

    Events.reset()
    Events.capture()

    update_screen_use_case.execute()