import json
from dataclasses import dataclass, asdict
from math import sqrt, sin, pi
from typing import TypeAlias

Point: TypeAlias = tuple[float, float]


@dataclass
class PolygonParams:
    n: int
    start: Point
    end: Point


class Polygon:
    def __init__(self, params: PolygonParams):
        self.__params = params

    @property
    def params(self):
        return self.__params

    @property
    def radius(self) -> float:
        xs, ys = self.__params.start
        xe, ye = self.__params.end
        return sqrt((xe - xs) ** 2 + (ye - ys) ** 2)

    @property
    def area(self) -> float:
        n = self.__params.n
        r = self.radius
        return (n * r ** 2) * sin(pi * 2 / n) / 2


class PolygonFactory:
    def __init__(self):
        self.__polygons: dict[str, Polygon] = {}

    @staticmethod
    def __to_key(params: PolygonParams) -> str:
        return json.dumps(asdict(params))

    def create(self, params: PolygonParams) -> Polygon:
        key = PolygonFactory.__to_key(params)
        if not self.__polygons.get(key):
            self.__polygons[key] = Polygon(params)
        return self.__polygons.get(key)

    def __len__(self):
        return len(self.__polygons)


if __name__ == "__main__":
    square_params = PolygonParams(n=2, start=(0.0, 0.0), end=(1.0, 2.0))
    polygon_factory = PolygonFactory()
    first_square = polygon_factory.create(square_params)
    second_square = polygon_factory.create(square_params)
    print(f"Second square is the first one: {id(first_square) == id(second_square)}")
    print(f"Length stays one ofter putting 2 objects with equal params: {len(polygon_factory) == 1}")
