from abc import ABC, abstractmethod
from typing import Optional
import re


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: "Handler") -> "Handler":
        ...

    @abstractmethod
    def handle(self, message: str) -> Optional[str]:
        ...


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, message: str) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(message)
        return None


class SwearWordsHandler(AbstractHandler):
    def handle(self, message: str) -> Optional[str]:
        pattern = r"\*{3,}"
        contains_swear_words = bool(re.search(pattern, message))
        if contains_swear_words:
            return "Message contains swear words"
        return super().handle(message)


class TooShortMessageHandler(AbstractHandler):
    def handle(self, message: str) -> Optional[str]:
        is_short = len(message) < 5
        if is_short:
            return "Message is too short"
        return super().handle(message)


class TooLongMessageHandler(AbstractHandler):
    def handle(self, message: str) -> Optional[str]:
        is_long = len(message) > 20
        if is_long:
            return "Message is too long"
        return super().handle(message)


if __name__ == "__main__":
    swear_words = SwearWordsHandler()
    too_short = TooShortMessageHandler()
    too_long = TooLongMessageHandler()
    swear_words.set_next(too_short).set_next(too_long)
    print(swear_words.handle("You better not mess up with me, ******"))
    print("-"*28)
    print(swear_words.handle("OK"))
    print("-"*28)
    print(swear_words.handle("Very long message without meaningful sense"))
