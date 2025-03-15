from src.enterprise.value_objects import Vector, Color

from src.enterprise.pillar_entity import PillarEntity

from src.application.repositories import IPillarRepository

from src.application.renders import IRender

from src.settings import Settings

class CreatePillarUseCase:

    def __init__(self, pillar_repository: IPillarRepository):
        self.pillar_repository = pillar_repository

    def select_pillar(self, pillar: PillarEntity):
        for p in self.pillar_repository.all():
            p.set_selected(False)
        pillar.set_selected(True)

    def execute(self, position: Vector, color: Color) -> PillarEntity:
        id = self.pillar_repository.generate_id()
        pillar = PillarEntity(id, position, color)
        self.select_pillar(pillar)
        self.pillar_repository.add(pillar)
        return pillar

class UpdateSelectedPillarPositionUseCase:

    def __init__(self, pillar_repository: IPillarRepository):
        self.pillar_repository = pillar_repository
    
    def get_selected_pillar(self):
        pillar = next((p for p in self.pillar_repository.all() if p.selected), None)
        return pillar

    def execute(self, new_position: Vector):
        selected_pillar = self.get_selected_pillar()
        if selected_pillar:
            selected_pillar.position = new_position

class DescelectAllPillarsUseCase:

    def __init__(self, pillar_repository: IPillarRepository):
        self.pillar_repository = pillar_repository

    def execute(self):
        for p in self.pillar_repository.all():
            p.set_selected(False)

class RenderPillarsUseCase:

    def __init__(self, pillar_repository: IPillarRepository, render: IRender):
        self.pillar_repository = pillar_repository
        self.render = render
    
    def execute(self, color: Color):
        for p in self.pillar_repository.all():
            tamanho_pixels = p.tamanho * Settings.PIXELS_POR_METRO
            self.render.quad(p.position, tamanho_pixels, color)