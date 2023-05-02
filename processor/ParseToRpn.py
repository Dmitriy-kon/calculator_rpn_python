from typing import Callable


class ParseToRpn:
    # PRIORITY: dict[int, list[str]] = {1: ['+', '-'], 2: ['*', '/'], 3: ['^']}

    def __init__(self):
        self.postfix: list = []
        self.operators: list = []

    @staticmethod
    def is_operator(operator: str):
        return operator in ['+', '-', '*', '/', '^']

    @staticmethod
    def get_priority(expr: str) -> int:
        if expr == "^":
            return 3
        elif expr in ['*', '/']:
            return 2
        elif expr in ['+', '-']:
            return 1
        elif expr == "(":
            return 0

    @staticmethod
    def parse_to_list(s):
        delims = ["+", "-", "*", "/", "(", ")", "^"]
        lex = []
        tmp = ""
        for a in s:
            if a != " ":
                if a in delims:
                    if tmp != "":
                        lex += [tmp]
                    lex.append(a)
                    tmp = ""
                else:
                    tmp += a
        if tmp != "":
            lex += [tmp]
        return lex

    def get_pol_notation(self, expr: str) -> str:
        expr: list = self.parse_to_list(expr)

        for element in expr:
            if element.isdigit() or element.isalpha():
                self.postfix.append(element)

            elif element == '(':
                self.operators.append(element)

            elif element == ')':
                while self.operators[-1] != '(':
                    self.postfix.append(self.operators.pop())
                self.operators.pop()

            elif self.is_operator(element):
                while self.operators and \
                        self.get_priority(self.operators[-1]) >= self.get_priority(element):
                    self.postfix.append(self.operators.pop())
                self.operators.append(element)
            else:
                raise ValueError(f"Не верный символ {element}")
        while self.operators:
            self.postfix.append(self.operators.pop())

        return ' '.join(i for i in self.postfix)


rpn = ParseToRpn()
expr = '21 - 7 * 8 / (7 - 2)'
res = rpn.get_pol_notation(expr)
print(res)
