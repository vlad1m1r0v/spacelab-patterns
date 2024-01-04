from abc import ABC, abstractmethod

WIDTH = 20
FULL_WIDTH = WIDTH


class Document(ABC):
    @abstractmethod
    def make_content_body(self):
        pass

    def make_content(self):
        global WIDTH, FULL_WIDTH
        name = self.__class__.__name__
        FULL_WIDTH = WIDTH + len(name)
        print(f"{'*' * int(WIDTH / 2)}{name.upper()}{'*' * int(WIDTH / 2)}\n\n")
        self.make_content_body()


def to_end(text: str):
    return f"{' ' * (FULL_WIDTH - len(text))}{text}"


class Diploma(Document):
    def __init__(self,
                 first_name: str,
                 last_name: str,
                 university: str,
                 speciality: str,
                 degree: str
                 ):
        self.full_name = f"{first_name} {last_name}"
        self.university = university
        self.speciality = speciality
        self.degree = degree

    def make_content_body(self):
        print(to_end(self.full_name))
        print(to_end(self.university))
        print(to_end(self.speciality))
        print(to_end(self.degree))


if __name__ == "__main__":
    diploma = Diploma(first_name="Brain",
                      last_name="Hopkins",
                      university="MIT",
                      speciality="Computer Science",
                      degree="Master Degree")
    diploma.make_content()
