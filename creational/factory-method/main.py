from abc import ABC, abstractmethod


class Language:
    def __init__(self, example):
        self._example = example

    def get_example(self):
        return self._example


class Ukrainian(Language):
    def __init__(self):
        super().__init__("Це приклад української мови")


class Spanish(Language):
    def __init__(self):
        super().__init__("Este es un ejemplo de español")


class Capital:
    def __init__(self, name):
        self._name = name

    def get_name(self) -> str:
        return self._name


class Kyiv(Capital):
    def __init__(self):
        super().__init__("Kyiv")


class Madrid(Capital):
    def __init__(self):
        super().__init__("Madrid")


class Country(ABC):
    @abstractmethod
    def get_language(self) -> Language:
        pass

    @abstractmethod
    def get_capital(self) -> Capital:
        pass

    def info(self) -> str:
        return (f"Our capital is {self.get_capital().get_name()}."
                f" Here is example of our language: {self.get_language().get_example()}.")


class Ukraine(Country):
    def get_language(self) -> Language:
        return Ukrainian()

    def get_capital(self) -> Capital:
        return Kyiv()


class Spain(Country):
    def get_language(self) -> Language:
        return Spanish()

    def get_capital(self) -> Capital:
        return Madrid()


if __name__ == "__main__":
    num = int(input())
    match num:
        case 0:
            country = Ukraine()
            print(country.info())
        case 1:
            country = Spain()
            print(country.info())