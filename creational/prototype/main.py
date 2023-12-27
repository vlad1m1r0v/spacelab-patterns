from abc import ABC, abstractmethod
from copy import deepcopy


class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class Person(Prototype):
    def __init__(self, height: int, weight: int):
        self.__height = height
        self.__weight = weight

    def set_height(self, height: int):
        self.__height = height

    def set_weight(self, weight: int):
        self.__weight = weight

    def __str__(self):
        return f"weight: {self.__weight} kg\n" \
               f"height: {self.__height} sm"

    def clone(self):
        return deepcopy(self)


if __name__ == "__main__":
    first_person = Person(height=185, weight=80)
    second_person = first_person.clone()
    second_person.set_weight(70)
    second_person.set_height(170)
    print('First person')
    print(first_person, '\n')
    print('Second person which was copied from first person')
    print(second_person)
