from src.enterprise.value_objects import Vector

class GameObjectEntity:

    def __init__(self, id: int):
        self.id : int = id

    def set_selected(self, on: bool) -> None:
        pass

    def set_hightlight(self, on: bool) -> None:
        pass

    def is_over(self, position: Vector) -> bool:
        pass

    def update(self) -> None:
        pass

    def render(self) -> None:
        pass