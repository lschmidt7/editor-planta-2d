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

from src.infrastructure.renders import Render

render = Render()

create_terrain_use_case = CreateTerrainUseCase()
render_terrain_use_case = RenderTerrainUseCase(render)

create_screen_use_case = CreateScreenUseCase()
update_screen_use_case = UpdateScreenUseCase(render)

init_screen_use_case = InitScreenUseCase(render)
draw_screen_use_case = DrawScreenUseCase(render)