from src.events import Events

from src.di.dependency_injection import (
    create_screen_use_case,
    init_screen_use_case,
    draw_screen_use_case,
    update_screen_use_case,
    create_terrain_use_case,
    render_terrain_use_case,
    create_pillar_use_case,
    render_pillars_use_case,
    update_selected_pillar_position_use_case,
    descelect_all_pillars_use_case
)

from src.enterprise.value_objects import Vector, Color

terrain_entity = create_terrain_use_case.execute(12, 25)

screen_entity = create_screen_use_case.execute(terrain_entity)

init_screen_use_case.execute(screen_entity)

while not Events.QUIT:
    draw_screen_use_case.execute()

    render_terrain_use_case.execute(terrain_entity, Color(35,35,35))

    render_pillars_use_case.execute(Color(255,100,0))

    Events.reset()
    Events.capture()

    if Events.MOUSE_LEFT_BUTTON_DOWN:
        create_pillar_use_case.execute(Events.MOUSE_POS, Color(255,100,0))
    
    if Events.MOUSE_LEFT_BUTTON_UP:
        descelect_all_pillars_use_case.execute()
    
    update_selected_pillar_position_use_case.execute(Events.MOUSE_POS)

    update_screen_use_case.execute()