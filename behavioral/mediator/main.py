from abc import ABC, abstractmethod
from enum import StrEnum, auto
from random import choice
from time import sleep
from typing import List, Set
from uuid import uuid4


class OrderType(StrEnum):
    FOOD = auto()
    BINGE = auto()


class Order:
    def __init__(self, order_type: OrderType):
        self.id = uuid4()
        self.type = order_type

    def __str__(self):
        return f"order № {self.id}"


class Event(StrEnum):
    GET_ORDER = auto()
    FINISH_ORDER = auto()


class WorkerType(StrEnum):
    WAITER = auto()
    CHIEF = auto()
    BARMAN = auto()


class Mediator(ABC):
    @abstractmethod
    def notify(self, worker: "Worker", order: Order, event: Event):
        ...

    @abstractmethod
    def add_worker(self, worker: "Worker") -> None:
        ...

    @abstractmethod
    def remove_worker(self, worker: "Worker") -> None:
        ...


class Worker(ABC):
    def __init__(self, name: str, m: Mediator):
        self.mediator = m
        self.name = name
        self.orders = []
        mediator.add_worker(self)

    @abstractmethod
    def take_order(self, order: Order):
        ...

    @abstractmethod
    def finish_order(self, order: Order):
        ...

    @abstractmethod
    def type(self) -> WorkerType:
        ...

    def get_orders_id(self) -> List[int]:
        return [order.id for order in self.orders]


class Waiter(Worker):
    def __init__(self, name: str, m: Mediator):
        super().__init__(name, m)

    def take_order(self, order: Order):
        sleep(0.5)
        print(f"Waiter {self.name} took {order}")
        self.orders.append(order)
        self.mediator.notify(self, order, Event.GET_ORDER)

    def finish_order(self, order: Order):
        sleep(0.5)
        print(f"Waiter {self.name} gave {order} to the client")
        print("-" * 80)
        self.orders.remove(order)

    def type(self) -> WorkerType:
        return WorkerType.WAITER


class Barman(Worker):
    def __init__(self, name: str, m: Mediator):
        super().__init__(name, m)

    def take_order(self, order: Order):
        sleep(0.5)
        print(f"Barman {self.name} took {order}")
        self.orders.append(order)
        self.processing_order()

    def finish_order(self, order: Order):
        sleep(2.0)
        print(f"Barman {self.name} fulfilled {order}")
        self.mediator.notify(self, order, Event.FINISH_ORDER)

    def processing_order(self):
        sleep(0.5)
        order = self.orders.pop()
        print(f"Barman {self.name} is doing {order}")
        self.finish_order(order)

    def type(self) -> WorkerType:
        return WorkerType.BARMAN


class Chief(Worker):
    def __init__(self, name: str, m: Mediator):
        super().__init__(name, m)

    def take_order(self, order: Order):
        sleep(0.5)
        print(f"Chief {self.name} took {order}")
        self.orders.append(order)
        self.processing_order()

    def finish_order(self, order: Order):
        sleep(2.0)
        print(f"Chief {self.name} fulfilled {order}")
        self.mediator.notify(self, order, Event.FINISH_ORDER)

    def processing_order(self):
        sleep(0.5)
        order = self.orders.pop()
        print(f"Chief {self.name} is doing {order}")
        self.finish_order(order)

    def type(self) -> WorkerType:
        return WorkerType.CHIEF


class WorkersMediator(Mediator):
    def __init__(self):
        self.workers: dict[WorkerType, Set[Worker]] = {WorkerType.WAITER: set(),
                                                       WorkerType.BARMAN: set(),
                                                       WorkerType.CHIEF: set()}

    def add_worker(self, worker: Worker):
        self.workers[worker.type()].add(worker)

    def remove_worker(self, worker: Worker):
        self.workers[worker.type()].remove(worker)

    def notify(self, worker: Worker, order: Order, event: Event):
        match event:
            case Event.GET_ORDER:
                if order.type is OrderType.FOOD:
                    chef = choice(list(self.workers.get(WorkerType.CHIEF)))
                    chef.take_order(order)
                else:
                    barman = choice(list(self.workers.get(WorkerType.BARMAN)))
                    barman.take_order(order)
            case Event.FINISH_ORDER:
                for waiter in self.workers[WorkerType.WAITER]:
                    if order.id in waiter.get_orders_id():
                        waiter.finish_order(order)
                        break


if __name__ == "__main__":
    mediator = WorkersMediator()
    waiter1 = Waiter("Anastasia", mediator)
    waiter2 = Waiter("Maria", mediator)
    barmen1 = Barman("Jacob", mediator)
    barmen2 = Barman("Mason", mediator)
    chief = Chief("Gordon", mediator)

    orders = [Order(choice([OrderType.FOOD, OrderType.BINGE])) for _ in range(10)]
    for it in orders:
        choice([waiter1, waiter2]).take_order(it)
