from abc import abstractmethod, ABC
from enum import StrEnum, auto
from typing import Union


class BaseLayer(StrEnum):
    T_SHIRT = auto()
    LONG_SLEEVE = auto()
    SINGLET = auto()


class UpperLayer(StrEnum):
    JACKET = auto()
    SWEATER = auto()
    HOODIE = auto()


class Pants(StrEnum):
    JEANS = auto()
    JOGGERS = auto()
    SHORTS = auto()


class Sneakers(StrEnum):
    VANS = auto()
    CONVERSE = auto()
    DR_MARTENS = auto()


class Look:
    def __init__(self):
        self.base_layer = None
        self.upper_layer = None
        self.pants = None
        self.sneakers = None

    def __str__(self):
        info = f"base layer: {self.base_layer}\n" \
               f"upper layer: {self.upper_layer}\n" \
               f"pants: {self.pants}\n" \
               f"sneakers: {self.sneakers}"
        return info


class Builder(ABC):
    @abstractmethod
    def set_base_layer(self) -> None: pass

    @abstractmethod
    def set_upper_layer(self) -> None: pass

    @abstractmethod
    def set_pants(self) -> None: pass

    @abstractmethod
    def set_sneakers(self) -> None: pass

    @abstractmethod
    def get_look(self) -> Look: pass


class JohnLookBuilder(Builder):
    def __init__(self):
        self.__look = Look()

    def set_base_layer(self) -> None:
        self.__look.base_layer = BaseLayer.SINGLET

    def set_upper_layer(self) -> None:
        self.__look.upper_layer = UpperLayer.JACKET

    def set_pants(self) -> None:
        self.__look.pants = Pants.JEANS

    def set_sneakers(self) -> None:
        self.__look.sneakers = Sneakers.DR_MARTENS

    def get_look(self) -> Look:
        return self.__look


class DrakeLookBuilder(Builder):
    def __init__(self):
        self.__look = Look()

    def set_base_layer(self) -> None:
        self.__look.base_layer = BaseLayer.LONG_SLEEVE

    def set_upper_layer(self) -> None:
        self.__look.upper_layer = UpperLayer.SWEATER

    def set_pants(self) -> None:
        self.__look.pants = Pants.JOGGERS

    def set_sneakers(self) -> None:
        self.__look.sneakers = Sneakers.VANS

    def get_look(self) -> Look:
        return self.__look


class AntonyLookBuilder(Builder):
    def __init__(self):
        self.__look = Look()

    def set_base_layer(self) -> None:
        self.__look.base_layer = BaseLayer.T_SHIRT

    def set_upper_layer(self) -> None:
        self.__look.upper_layer = UpperLayer.HOODIE

    def set_pants(self) -> None:
        self.__look.pants = Pants.SHORTS

    def set_sneakers(self) -> None:
        self.__look.sneakers = Sneakers.CONVERSE

    def get_look(self) -> Look:
        return self.__look


class Stylist:
    def __init__(self):
        self.__builder: Union[Builder, None] = None

    def set_builder(self, b: Builder):
        self.__builder = b

    def make_look(self):
        if self.__builder is None:
            raise ValueError("Builder didn't set")
        self.__builder.set_base_layer()
        self.__builder.set_upper_layer()
        self.__builder.set_pants()
        self.__builder.set_sneakers()


if __name__ == "__main__":
    stylist = Stylist()
    for it in (JohnLookBuilder, AntonyLookBuilder, DrakeLookBuilder):
        builder = it()
        stylist.set_builder(builder)
        stylist.make_look()
        look = builder.get_look()
        print(look, '\n')
