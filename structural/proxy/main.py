from abc import ABC, abstractmethod


class IPerson(ABC):
    @abstractmethod
    def personal_info(self) -> None:
        pass


class Person(IPerson):
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    def personal_info(self) -> None:
        print(f"My name is {self.__name}. I am  {self.__age} y.o.")


class PersonProxy(IPerson):
    def __init__(self, p: Person):
        self.__p = p

    def personal_info(self) -> None:
        adult_or_not = "" if self.__p.age >= 18 else "not "
        self.__p.personal_info()
        print(f"I am {adult_or_not}adult.")


if __name__ == "__main__":
    mike = Person("Mike", 16)
    proxy = PersonProxy(mike)
    proxy.personal_info()
