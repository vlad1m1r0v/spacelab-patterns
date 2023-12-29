from abc import ABC, abstractmethod


class Component(ABC):

    @abstractmethod
    def size(self) -> int:
        pass


class File(Component):
    def __init__(self, name: str, size: int):
        self.__name = name
        self.__size = size

    def size(self):
        return self.__size


class Folder(Component):
    def __init__(self, name, c: list[Component]):
        self.__name = name
        self.__components = c

    def size(self):
        return sum(c.size() for c in self.__components)

    def add(self, c: Component):
        self.__components.append(c)


if __name__ == "__main__":
    resume = File("resume.doc", 1024)
    cover_letter = File("abstract.docx", 2048)
    reference = File("article.pdf", 4096)
    documents = Folder("Documents", [resume, cover_letter, reference])

    todo = File("todo.txt", 256)
    screenshot = File("screenshot.png", 2048)
    desktop = Folder("Desktop", [todo, screenshot])

    user = Folder("User", [desktop, documents])
    print(user.size())
