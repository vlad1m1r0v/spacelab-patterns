import random


class Teacher:
    def __init__(self, name: str):
        self.__name = name

    def assign_test(self):
        print(f"Teacher {self.__name} assigned test.")


class Student:
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def complete_test(self):
        print(f"Student {self.__name} completed test.")


class GoogleForm:
    @staticmethod
    def graduate_test(student_name: str):
        print(f"Google Form automatically graduated test of student {student_name}. "
              f"Result: {random.randint(60, 100)}")


class Test:
    def __init__(self):
        self.__teacher = Teacher("Svitlana Shevchenko")
        self.__student = Student("Taras Voloshyn")
        self.__google_form = GoogleForm

    def simulate(self):
        self.__teacher.assign_test()
        self.__student.complete_test()
        self.__google_form.graduate_test(self.__student.name)


if __name__ == "__main__":
    test = Test()
    test.simulate()
