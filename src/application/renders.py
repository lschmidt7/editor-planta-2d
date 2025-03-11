from abc import ABC, abstractmethod

from src.enterprise.pillar_entity import PillarEntity
from src.enterprise.wall_entity import WallEntity
from src.enterprise.value_objects import Vector, Color

class IScreenRender(ABC):

    @abstractmethod
    def initialize(self, width: int, height: int, title: str) -> None:
        pass

    @abstractmethod
    def render(self) -> None:
        pass

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def line(self, start: Vector, end: Vector, color: Color) -> None:
        pass

class IPillarRender(ABC):

    @abstractmethod
    def render(self, pillar: PillarEntity) -> None:
        pass

class IWallRender(ABC):

    @abstractmethod
    def render(self, wall : WallEntity) -> None:
        pass

class ITerrainRenderer(ABC):

    @abstractmethod
    def render(self) -> None:
        pass