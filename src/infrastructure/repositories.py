from typing import List

from src.enterprise.pillar_entity import PillarEntity
from src.enterprise.wall_entity import WallEntity

from src.application.repositories import IPillarRepository, IWallRepository

class PillarRepository(IPillarRepository):

    def __init__(self):
        self.id = 0
        self.pillars : List[PillarEntity] = []
    
    def generate_id(self):
        self.id += 1
        return self.id

    def add(self, pillar: PillarEntity):
        self.pillars.append(pillar)
    
    def all(self):
        return self.pillars

class WallRepository(IWallRepository):

    def __init__(self):
        self.id = 0
        self.walls : List[WallEntity] = []
    
    def generate_id(self):
        self.id += 1
        return self.id

    def add(self, wall: WallEntity):
        self.walls.append(wall)
    
    def all(self):
        return self.walls