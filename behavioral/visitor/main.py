import math
from abc import ABC, abstractmethod
from enum import Enum


class Product(ABC):
    @abstractmethod
    def accept(self, cashier) -> float:
        pass


class Quality(Enum):
    GOOD = 1.2
    MEDIUM = 1.0
    LOW = 0.8


class Apple(Product):
    price_per_kg = 20

    def __init__(self, quality: Quality, kg: float):
        self.quality = quality
        self.kg = kg

    def accept(self, cashier) -> float:
        return cashier.visit_apple(self)


class Sugar(Product):
    price_per_50kg = 1600

    def __init__(self, kg: float):
        self.kg = kg

    def accept(self, cashier) -> float:
        return cashier.visit_sugar(self)


class Cashier(ABC):
    @abstractmethod
    def visit_apple(self, apple: Apple):
        pass

    @abstractmethod
    def visit_sugar(self, sugar: Sugar):
        pass


class ConcreteCashier(Cashier):
    def visit_apple(self, apple: Apple):
        return apple.kg * apple.price_per_kg * apple.quality.value

    def visit_sugar(self, sugar: Sugar):
        return sugar.price_per_50kg / 50 * sugar.kg * (1 - min(math.log(sugar.kg, 200), 0.5))

    def total_price(self, products: list[Product]):
        result = 0.0
        for p in products:
            result += p.accept(self)
        return result


if __name__ == "__main__":
    apples = Apple(Quality.GOOD, 10)
    sugar = Sugar(100)
    cashier = ConcreteCashier()
    result = cashier.total_price([apples, sugar])
    print(f"Result: {result}")
