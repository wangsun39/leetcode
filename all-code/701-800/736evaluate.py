import copy
from typing import List
class Solution:
    def evaluate(self, expression: str) -> int:
        def find_end(start):
            if start[0] != '(':
                end = start.find(' ')
                return end if end != -1 else len(start)
            stack = 1
            for i, e in enumerate(start[1:]):
                if e == '(':
                    stack += 1
                elif e == ')':
                    stack -= 1
                    if stack == 0:
                        return 1 + i
        def find(expr: str):
            if expr[0].isdigit():
                end = expr.find(' ')
                return end if end != -1 else expr
        def get_variable(expr: str):
            end = expr.find(' ')
            return expr[:end] if end != -1 else expr
        def get_number(expr: str):
            return int(get_variable())
        def get_segment(expr: str):
            ans = 1
            stack = 1
            while stack > 0:
                if expr[ans] == '(':
                    stack += 1
                elif expr[ans] == ')':
                    stack -= 1
                ans += 1
            return ans
        def eval(expr, d) -> [int, int]:
            if expr[0].isalpha():
                name = get_variable(expr)
                return [d[name], len(name) + 1]
            elif expr[0].isdigit():
                name = get_variable(expr)
                return [int[name], len(name) + 1]
            else:
                name = get_segment(expr)
                return [calc(name), len(name) + 1]
        def calc(expr: str, d):
            dic = copy.deepcopy(d)

            if expr.startswith('(add'):
                [val1, pos] = eval(expr[5:])
                # if expr[5].isalpha():
                #     name = get_variable(expr[5:])
                #     val1 = dic[name]
                #     pos = len(name) + 5 + 1
                # elif expr[5].isdigit():
                #     name = get_variable(expr[5:])
                #     val1 = int(name)
                #     pos = len(name) + 5 + 1
                # else:
                #     name = get_segment(expr[5:])
                #     val1 = calc(name)
                #     pos = len(name) + 5 + 1
                [val2, _] = eval(expr[pos:])

                # if expr[pos].isalpha():
                #     name = expr[pos:]
                #     val2 = dic[name]
                # elif expr[pos].isdigit():
                #     name = expr[pos:]
                #     val2 = int(name)
                # else:
                #     name = get_segment(expr[pos:])
                #     val2 = calc(name)

                return val1 + val2


            elif expr.startswith('(let'):
                pos = 5
                while pos < len(expr):
                    name = get_variable(expr[5:])
                    pos += len(name) + 1


            else:
                pass

so = Solution()
print(so.evaluate([5,10,-5]))

