from abc import ABC, abstractmethod
from typing import Optional


class State(ABC):
    student: Optional["Student"] = None

    def execute(self):
        print(f"\nCurrent state: {self.__class__.__name__}")
        self.handle()

    @abstractmethod
    def handle(self):
        pass


class Student:
    state = None

    def __init__(self, name: str, state: State):
        self.name = name
        self.set_state(state)

    def set_state(self, st: State):
        self.state = st
        self.state.student = self
        self.start()

    def start(self):
        self.state.execute()


class WakeUp(State):
    def handle(self):
        print(f"It's 7:30 AM, {self.student.name} woke up")
        self.student.set_state(GoToUniversity())


class GoToUniversity(State):
    def handle(self):
        print(f"It's 8:00 AM, {self.student.name} goes to the metro station and then gets to university")
        self.student.set_state(AttendLectures())


class AttendLectures(State):
    def handle(self):
        print(f"It's 8:30 AM, the lectures for {self.student.name} have just begun")
        self.student.set_state(GoToDormitory())


class GoToDormitory(State):
    def handle(self):
        print(f"It's 3:45 PM, the lectures for {self.student.name} ended and he goes to the dorm")
        self.student.set_state(OrderFood())


class OrderFood(State):
    def handle(self):
        print(f"It's 4:30 PM, {self.student.name} is hungry, he decides to order pizza")
        self.student.set_state(DoHomeTask())


class DoHomeTask(State):
    def handle(self):
        print(f"It's 5:30 PM, {self.student.name} starts doing his homework")
        self.student.set_state(FallAsleep())


class FallAsleep(State):
    def handle(self):
        print(f"It's 11 PM, {self.student.name} students daily routine is over. He fall asleep")


if __name__ == "__main__":
    student = Student(name="Martin", state=WakeUp())
