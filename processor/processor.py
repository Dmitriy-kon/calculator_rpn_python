from processor.CalculateRpn import CalculateRpn
from processor.ParseToRpn import ParseToRpn


# from CalculateRpn import CalculateRpn
# from ParseToRpn import ParseToRpn


class Processor:
    def __init__(self):
        self.calculate_rpn: CalculateRpn = CalculateRpn()
        self.rpn: ParseToRpn = ParseToRpn()

    def check_postfix(self, math_expr: str) -> bool:
        pass

    def transform_to_postfix(self, math_expr: str) -> str:
        res = self.rpn.get_pol_notation(math_expr)
        return res

    def calculate(self, math_expr: str) -> int:
        post_fix = self.transform_to_postfix(math_expr)
        res = self.calculate_rpn.execute_opr(post_fix)
        return res
