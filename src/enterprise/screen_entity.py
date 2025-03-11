from src.enterprise.value_objects import Color

class ScreenEntity:

    def __init__(self, width: int, height: int, background: Color, title: str):
        self.width = width
        self.height = height
        self.background = background
        self.title = title