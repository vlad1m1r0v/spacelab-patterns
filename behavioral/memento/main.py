import time
from abc import ABC, abstractmethod
from collections import deque
from time import strftime, localtime
from typing import Deque


class Memento(ABC):
    @abstractmethod
    def get_state(self):
        pass

    @abstractmethod
    def get_time(self):
        pass


class BalanceMemento(Memento):
    def __init__(self, amount: float):
        self._amount = amount
        self._time = strftime("%H:%M:%S", localtime())
        print(f"New save. Amount = {self._amount}, Time = {self._time}")

    def get_state(self):
        return self._amount

    def get_time(self):
        return self._time


class Balance:
    def __init__(self, amount: float):
        self._amount: float = amount

    @property
    def amount(self):
        return self._amount

    def replenish(self, cash: float):
        print(f"Replenish money: {cash}")
        self._amount += cash

    def withdraw(self, cash: float):
        print(f"Withdraw money: {cash}")
        self._amount -= cash

    def save(self) -> Memento:
        return BalanceMemento(self.amount)

    def restore(self, m: Memento):
        state = m.get_state()
        self._amount = state


class User:
    def __init__(self, b: Balance):
        self._balance = b
        self._mementos: Deque[Memento] = deque()

    def save(self):
        self._mementos.append(self._balance.save())

    def restore(self):
        if not len(self._mementos):
            return
        prev = self._mementos.pop()
        self._balance.restore(prev)


if __name__ == "__main__":
    balance = Balance(2_000)
    print(f"Initial balance: {balance.amount}")
    user = User(balance)
    # after init
    user.save()
    balance.replenish(500)
    # after replenish
    user.save()
    print(f"Balance after replenish: {balance.amount}")
    time.sleep(5.0)
    balance.withdraw(200)
    # after withdraw+ ge
    user.save()
    print(f"Balance after withdraw: {balance.amount}")
    user.restore()
    print(f"Balance after first restore: {balance.amount}")
    user.restore()
    print(f"Balance after second restore: {balance.amount}")
