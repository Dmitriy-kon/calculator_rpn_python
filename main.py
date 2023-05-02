from typing import Callable
from processor import Processor


class Memory:

    def __init__(self):
        self.memory: list = []

    def add_to_memory(self, math_expr: str) -> None:
        if len(self.memory) > 3:
            self.memory.pop(0)
        self.memory.append(math_expr)

    def get_memory(self) -> list:
        return self.memory


class Calculator:
    def __init__(self):
        self.processor: Processor = Processor()
        self.memory: Memory = Memory()

    def start_calculator(self, math_expr: str) -> int:
        res = self.processor.calculate(math_expr)
        return res

    def print_last_operation(self):
        pass


if __name__ == '__main__':
    calculator = Calculator()

    pol = "(1 + 8) * 20 + 8 - (6 ^ 2)"
    res = calculator.start_calculator(pol)
    print(res)
