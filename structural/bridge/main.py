import json
import logging
from abc import ABC, abstractmethod
from typing import Union


class Reader(ABC):
    @abstractmethod
    def read(self):
        pass


class TextReader(Reader):
    def read(self):
        with open("file.txt", "r") as file:
            line = file.readline()
            return line.split("example: ")[1]


class JSONReader(Reader):
    def read(self):
        with open("file.json", "r") as file:
            data = json.load(file)
            return data["example"]


class Printer(ABC):
    def __init__(self, r: Union[Reader, None]):
        self._reader = r

    def set_reader(self, r: Reader):
        self._reader = r

    @abstractmethod
    def print(self):
        pass


class DefaultPrinter(Printer):
    def __init__(self, r: Union[Reader, None] = None):
        super().__init__(r)

    def print(self):
        print(f"default print: {self._reader.read()}")


class LoggingPrinter(Printer):
    def __init__(self, r: Union[Reader, None] = None):
        logging.basicConfig(level=logging.DEBUG,
                            filemode='w',
                            format='%(asctime)s %(levelname)s %(message)s',
                            datefmt='%d %b %Y')
        super().__init__(r)

    def print(self):
        logging.info(f"logging: {self._reader.read()}")


if __name__ == "__main__":
    # init readers
    text_reader: Reader = TextReader()
    json_reader: Reader = JSONReader()
    # init printers
    default_printer: Printer = DefaultPrinter()
    logging_printer: LoggingPrinter = LoggingPrinter()
    # show examples with setting and switching readers for printers
    # set
    default_printer.set_reader(text_reader)
    default_printer.print()
    # switch
    default_printer.set_reader(json_reader)
    default_printer.print()
    # set
    logging_printer.set_reader(text_reader)
    logging_printer.print()
    # switch
    logging_printer.set_reader(json_reader)
    logging_printer.print()
