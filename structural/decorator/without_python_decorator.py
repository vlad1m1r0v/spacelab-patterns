class Text:
    def __init__(self, line: str):
        self._line = line

    def show(self):
        print(self._line)


class Decorator(Text):
    def __init__(self, txt: Text):
        self._text = txt

    def show(self):
        self._text.show()


class FramedTextDecorator(Decorator):
    def show(self):
        width = len(self._text._line) + 2
        print(width * "-")
        print(f"|{self._text._line}|")
        print(width * "-")


class ColoredTextDecorator(Decorator):
    def show(self):
        print("\033[34m")
        super().show()
        print("\033[0m")


if __name__ == "__main__":
    text = Text("My name is Artem, I am 21 years old")
    text.show()
    framed = FramedTextDecorator(text)
    framed.show()
    colored_and_framed = ColoredTextDecorator(framed)
    colored_and_framed.show()
