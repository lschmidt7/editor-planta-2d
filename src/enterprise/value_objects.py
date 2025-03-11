from typing import Tuple
import math

class Color:

    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b
    
    def tupple(self) -> Tuple:
        return (self.r, self.g, self.b)


class Vector:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y)
    
    def __floordiv__(self, value : float) -> 'Vector':
        return Vector(int(self.x / value), int(self.y / value))
    
    def __str__(self):
        return f'X: {self.x:.2f}m Y: {self.y:.2f}m'
    
    def toStr(self):
        return f'X: {self.x:.2f}m', f'Y: {self.y:.2f}m'
    
    def __mul__(self, value: float):
        return Vector(self.x * value, self.y * value)

    def tupple(self) -> Tuple:
        return (self.x, self.y)

    def distance(self, other: 'Vector') -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def unit(self) -> 'Vector':
        l = self.length()
        if l <= 0:
            return Vector(0,0)
        return Vector(self.x / l, self.y / l)