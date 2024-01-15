class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Plain(metaclass=SingletonMeta):
    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height


if __name__ == "__main__":
    p1 = Plain(width=10, height=10)
    p2 = Plain(width=20, height=20)
    print(f"p1 and p2 are the same objects: {str(id(p1) == id(p2))}")
