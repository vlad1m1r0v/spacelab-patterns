import random
from abc import ABC, abstractmethod


class Road(ABC):
    @abstractmethod
    def create(self, places: list[str]):
        pass


class RandomRoad(Road):
    def create(self, places: list[str]):
        return random.sample(places, len(places))


class ReverseRoad(Road):
    def create(self, places: list[str]):
        return places[::-1]


class Tourist:
    def __init__(self, road: Road):
        self._road = road

    def set_road(self, road: Road):
        self._road = road

    def walk(self, places: list[str]) -> str:
        return " -> ".join(self._road.create(places))


if __name__ == "__main__":
    road_places = ["Gym", "Park", "WC", "Pizzeria", "Library"]
    random_road = RandomRoad()
    reverse_road = ReverseRoad()
    tourist = Tourist(reverse_road)
    print(tourist.walk(road_places))
    tourist.set_road(random_road)
    print(tourist.walk(road_places))
