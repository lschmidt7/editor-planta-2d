from src.events import Events

from src.di.dependency_injection import (
    create_screen_use_case,
    init_screen_use_case,
    draw_screen_use_case,
    update_screen_use_case,
    create_terrain_use_case,
    render_terrain_use_case
)

from src.enterprise.pillar_entity import PillarEntity
from src.enterprise.value_objects import Vector, Color

from src.infrastructure.repositories import (
    PillarRepository, 
    WallRepository
)

pillar_repository = PillarRepository()
wall_repository = WallRepository()

terrain_entity = create_terrain_use_case.execute(12, 25)

screen_entity = create_screen_use_case.execute(terrain_entity)

init_screen_use_case.execute(screen_entity)

pillar_repository.add(PillarEntity(1, Vector(50, 50), Color(255,100,0)))

while not Events.QUIT:
    draw_screen_use_case.execute()

    render_terrain_use_case.execute(terrain_entity, Color(35,35,35))

    Events.reset()
    Events.capture()

    update_screen_use_case.execute()