from src.enterprise.value_objects import Vector, Color

from src.enterprise.pillar_entity import PillarEntity

from src.application.repositories import IPillarRepository

class CreatePillarUseCase:

    def __init__(self, pillar_repository: IPillarRepository):
        self.pillar_repository = pillar_repository

    def execute(self, position: Vector, color: Color):
        id = self.pillar_repository.generate_id()
        pillar = PillarEntity(id, position, color)