from abc import ABC, abstractmethod
from typing import List

from src.enterprise.pillar_entity import PillarEntity
from src.enterprise.wall_entity import WallEntity

class IPillarRepository(ABC):

    @abstractmethod
    def generate_id(self) -> int:
        pass

    @abstractmethod
    def add(self, pillar : PillarEntity) -> None:
        pass

    @abstractmethod
    def all(self) -> List[PillarEntity]:
        pass

class IWallRepository(ABC):

    @abstractmethod
    def generate_id(self) -> int:
        pass

    @abstractmethod
    def add(self, wall : WallEntity) -> None:
        pass

    @abstractmethod
    def all(self) -> List[WallEntity]:
        pass