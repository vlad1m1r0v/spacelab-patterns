import re
from collections.abc import Iterator, Iterable
from dataclasses import dataclass
from enum import Enum


class Token(Enum):
    SPACE = re.compile(r'\s+')
    ADD = re.compile(r'\+')
    SUBTRACT = re.compile(r'-')
    MULTIPLY = re.compile(r'\*')
    DIVIDE = re.compile(r'/')
    POW = re.compile(r'\^')
    OPEN_PARENS = re.compile(r'\(')
    CLOSE_PARENS = re.compile(r'\)')
    COMMA = re.compile(r',')
    IDENTIFIER = re.compile(r'[a-zA-Z_$][a-zA-Z0-9_$]*')
    NUMBER = re.compile(r'-?\d+(\.\d+)?')
    UNKNOWN = re.compile(r'.')


@dataclass
class MatchedToken:
    type: Token
    matched_at: int
    value: str


class ExpressionIterator(Iterator):
    def __init__(self, expr: str):
        self._expr = expr
        self._pos = 0

    def __next__(self):
        for t in Token:
            if self._pos >= len(self._expr):
                raise StopIteration()
            match = t.value.match(self._expr, self._pos)
            if match:
                value = match.group()
                self._pos += len(value)
                token = MatchedToken(type=t, matched_at=self._pos, value=value)
                return token


class Expression(Iterable):
    def __init__(self, expr: str):
        self._expr = expr

    def __iter__(self):
        return ExpressionIterator(self._expr)


if __name__ == "__main__":
    input_expr = input()
    instance_expr = Expression(input_expr)
    for token_expr in instance_expr:
        print(token_expr)
