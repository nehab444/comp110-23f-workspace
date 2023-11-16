"""Mutating and not mutating methods."""

from __future__ import annotations

__author__: str = "730645945"


class Point:
    """This class creates a Point."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0) -> None:
        """My constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """This function mutates a Point."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """This function creates a new point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point

    def __mul__(self, factor: int | float) -> Point:
        """This function creates a new point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point

    def __str__(self) -> str:
        """Creates a string."""
        return f"x: {self.x}; y: {self.y}"

    def __add__(self, factor: int | float) -> Point:
        """This function creates a new point."""
        new_point: Point = Point(self.x + factor, self.y + factor)
        return new_point
    
