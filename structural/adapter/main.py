import re
from functools import reduce


class NumberAdder:
    def __init__(self, nums: list[float]):
        self.__nums = nums

    def add(self) -> float:
        return reduce((lambda x, y: x + y), self.__nums)


class TextToNumberAdapter(NumberAdder):
    def __init__(self, text: str):
        pattern = r"-?\d+\.?\d*"
        nums_str = re.findall(pattern, text)
        nums = [float(num_str) for num_str in nums_str]
        super().__init__(nums)


if __name__ == "__main__":
    number_adder = NumberAdder([n ** 2 for n in range(10)])
    print("Added numbers from array give result:\n"
          f"{number_adder.add()}")
    txt = "I have 5 $, John has 10.5 $, Maria has 15 $"
    numbers_from_text_adder = TextToNumberAdapter(txt)
    print("Added extracted numbers from text give result:\n"
          f"{numbers_from_text_adder.add()}")
