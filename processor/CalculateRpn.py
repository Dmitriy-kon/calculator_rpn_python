from typing import Callable


class CalculateRpn:
    def __init__(self):
        self.stack = []
        self.operation: Operation = Operation()

    def execute_opr(self, math_expr: str) -> int:
        for token in math_expr.split():
            if token in "+/*-^":
                operand2 = self.stack.pop()
                operand1 = self.stack.pop()
                res = self.operation.operation(token)(operand1, operand2)

                self.stack.append(res)
            if token.isdigit():
                self.stack.append(int(token))

        return self.stack[0]


class Operation:
    def operation(self, operator: str) -> Callable:
        if operator == "+":
            return self.sum_
        elif operator == "-":
            return self.sub_
        elif operator == "*":
            return self.mult_
        elif operator == "/":
            return self.div_
        elif operator == "^":
            return self.exp_

    @staticmethod
    def sum_(a: int, b: int) -> int:
        return a + b

    @staticmethod
    def sub_(a: int, b: int) -> int:
        return a - b

    @staticmethod
    def mult_(a: int, b: int) -> int:
        return a * b

    @staticmethod
    def div_(a: int, b: int) -> int | float:
        return a / b

    @staticmethod
    def exp_(a: int, b: int) -> int | float:
        return a ** b
