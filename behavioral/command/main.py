from abc import ABC, abstractmethod
from typing import List


class Television:
    def __init__(self):
        self._is_turned_on: bool = False
        self._channel: int = 0
        self._volume: int = 15

    def toggle(self):
        self._is_turned_on = not self._is_turned_on
        print(f"Is turned on: {self._is_turned_on}")

    def enhance_volume(self):
        self._volume += 1
        print(f"Volume: {self._volume}")

    def reduce_volume(self):
        if self._volume > 0:
            self._volume -= 1
        print(f"Volume: {self._volume}")

    def next_channel(self):
        self._channel += 1
        print(f"Channel: {self._channel}")

    def previous_channel(self):
        if self._channel > 0:
            self._channel += 1
        print(f"Channel: {self._channel}")


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        ...


class ToggleCommand(Command):
    def __init__(self, tv: Television):
        self._tv = tv

    def execute(self) -> None:
        self._tv.toggle()


class EnhanceVolumeCommand(Command):
    def __init__(self, tv: Television):
        self._tv = tv

    def execute(self) -> None:
        self._tv.enhance_volume()


class ReduceVolumeCommand(Command):
    def __init__(self, tv: Television):
        self._tv = tv

    def execute(self) -> None:
        self._tv.enhance_volume()


class NextChannelCommand(Command):
    def __init__(self, tv: Television):
        self._tv = tv

    def execute(self) -> None:
        self._tv.next_channel()


class PreviousChannelCommand(Command):
    def __init__(self, tv: Television):
        self._tv = tv

    def execute(self) -> None:
        self._tv.previous_channel()


class Viewer:
    def __init__(self):
        self._commands: List[Command] = list()

    def add_command(self, cmd: Command):
        self._commands.append(cmd)

    def do_commands(self):
        while len(self._commands):
            cmd = self._commands.pop(0)
            cmd.execute()


if __name__ == "__main__":
    television = Television()
    viewer = Viewer()
    viewer.add_command(ToggleCommand(television))
    viewer.add_command(NextChannelCommand(television))
    viewer.add_command(NextChannelCommand(television))
    viewer.add_command(EnhanceVolumeCommand(television))
    viewer.add_command(ToggleCommand(television))
    viewer.do_commands()
