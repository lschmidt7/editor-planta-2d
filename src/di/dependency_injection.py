from src.application.usecases.terrain_use_cases import (
    CreateTerrainUseCase,
    RenderTerrainUseCase
)

from src.application.usecases.screen_use_cases import (
    CreateScreenUseCase,
    UpdateScreenUseCase,
    InitScreenUseCase,
    DrawScreenUseCase
)

from src.application.usecases.pillar_use_cases import (
    CreatePillarUseCase,
    UpdateSelectedPillarPositionUseCase,
    DescelectAllPillarsUseCase,
    RenderPillarsUseCase
)

from src.infrastructure.renders import Render

from src.infrastructure.repositories import PillarRepository

pillar_repository = PillarRepository()

render = Render()

create_terrain_use_case = CreateTerrainUseCase()
render_terrain_use_case = RenderTerrainUseCase(render)

create_screen_use_case = CreateScreenUseCase()
update_screen_use_case = UpdateScreenUseCase(render)
init_screen_use_case = InitScreenUseCase(render)
draw_screen_use_case = DrawScreenUseCase(render)

create_pillar_use_case = CreatePillarUseCase(pillar_repository)
render_pillars_use_case = RenderPillarsUseCase(pillar_repository, render)
update_selected_pillar_position_use_case = UpdateSelectedPillarPositionUseCase(pillar_repository)
descelect_all_pillars_use_case = DescelectAllPillarsUseCase(pillar_repository)