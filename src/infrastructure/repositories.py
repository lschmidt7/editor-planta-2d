from typing import List

from src.enterprise.pillar_entity import PillarEntity
from src.enterprise.wall_entity import WallEntity

from src.application.repositories import IPillarRepository, IWallRepository

class PillarRepository(IPillarRepository):

    def __init__(self):
        self.pillars : List[PillarEntity] = []
    
    def add(self, pillar: PillarEntity):
        self.pillars.append(pillar)
    
    def all(self):
        return self.pillars

class WallRepository(IWallRepository):

    def __init__(self):
        self.walls : List[WallEntity] = []
    
    def add(self, wall: WallEntity):
        self.walls.append(wall)
    
    def all(self):
        return self.walls