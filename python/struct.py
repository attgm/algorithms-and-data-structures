#! /usr/bin/env python3
from dataclasses import dataclass
import math

@dataclass
class Point:
    x: float
    y: float

def distance(p1: Point, p2: Point) -> float:
    return math.sqrt(math.pow(p1.x - p2.x, 2) + math.pow(p1.y - p2.y, 2))

def input_point() -> Point:
    x: float = float(input("x = "))
    y: float = float(input("y = "))
    p: Point = Point(x, y)
    return p

def main():
    print("p1:")
    p1: Point = input_point()
    print("p2:")
    p2: Point = input_point()

    d = distance(p1, p2)
    print(f"distance = {d:.3f}")

if __name__ == "__main__":
    main()
