"""Starry Night Sky with Mountains and Trees."""

__author__ = "730645945"

from turtle import Turtle, Screen, colormode, done
import random


def main() -> None:
    """The entrypoint of my scene."""
    colormode(255)
    leo: Turtle = Turtle()
    leo.speed(0)

    def draw_star(x: float, y: float, size: float) -> None:
        """Draw a star at the specified position with the given size."""
        leo.penup()
        leo.goto(x, y)
        leo.pendown()
        leo.fillcolor("yellow")
        leo.begin_fill()

        for _ in range(5):
            leo.forward(size)
            leo.right(144)

        leo.end_fill()

    def draw_mountain(x: float, y: float, mountain_height: float, mountain_base: float) -> None:
        """Draw a mountain at the specified position with the given height and base."""
        leo.penup()
        leo.goto(x, y)
        leo.pendown()
        leo.fillcolor("saddle brown")
        leo.begin_fill()

        leo.goto(x, y)
        leo.goto(x + mountain_base, y)
        leo.goto(x + mountain_base / 2, y + mountain_height)
        leo.goto(x, y)

        leo.end_fill()

    def draw_tree(x: float, y: float, trunk_height: float, trunk_width: float, canopy_height: float, canopy_radius: float) -> None:
        """Draw a tree at the specified position with the given trunk and canopy dimensions."""
        # Draw the tree trunk
        leo.penup()
        leo.goto(x, y)
        leo.pendown()
        leo.fillcolor("sienna")
        leo.begin_fill()

        for _ in range(2):
            leo.forward(trunk_width)
            leo.left(90)
            leo.forward(trunk_height)
            leo.left(90)

        leo.end_fill()

        # Draw the tree canopy
        leo.penup()
        leo.goto(x, y + trunk_height)
        leo.pendown()
        leo.fillcolor("forest green")
        leo.begin_fill()
        leo.circle(canopy_radius)
        leo.end_fill()

    def draw_starry_sky(num_stars: int) -> None:
        """Draw a starry night sky with the specified number of stars."""
        for _ in range(num_stars):
            x = random.uniform(-400, 400)
            y = random.uniform(-300, 300)
            size = random.uniform(1, 5)
            draw_star(x, y, size)

    screen = Screen()

    # Draw the night sky background
    leo.penup()
    leo.goto(-screen.window_width() / 2, screen.window_height() / 2)
    leo.pendown()
    leo.fillcolor("midnight blue")
    leo.begin_fill()

    for _ in range(2):
        leo.forward(screen.window_width())
        leo.right(90)
        leo.forward(screen.window_height())
        leo.right(90)

    leo.end_fill()

    # Draw the mountains
    draw_mountain(-100, -50, 100, 200)
    draw_mountain(100, -50, 100, 200)

    # Draw the river
    leo.penup()
    leo.goto(-screen.window_width() / 2, -100)
    leo.pendown()
    leo.fillcolor("blue")
    leo.begin_fill()
    leo.forward(screen.window_width())
    leo.right(90)
    leo.forward(200)
    leo.right(90)
    leo.forward(screen.window_width())
    leo.right(90)
    leo.forward(200)
    leo.end_fill()

    # Draw the stars in the night sky
    draw_starry_sky(150)

    # Draw trees
    draw_tree(-150, -50, 60, 5, 40, 20)
    draw_tree(50, -50, 70, 6, 50, 25)

    done()


if __name__ == "__main__":
    main()
