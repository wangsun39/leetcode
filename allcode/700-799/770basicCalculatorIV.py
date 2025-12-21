# 给定一个表达式如 expression = "e + 8 - a + 5" 和一个求值映射，如 {"e": 1}（给定的形式为 evalvars = ["e"] 和 evalints = [1]），返回表示简化表达式的标记列表，例如 ["-1*a","14"]
#
# 表达式交替使用块和符号，每个块和符号之间有一个空格。
# 块要么是括号中的表达式，要么是变量，要么是非负整数。
# 变量是一个由小写字母组成的字符串（不包括数字）。请注意，变量可以是多个字母，并注意变量从不具有像 "2x" 或 "-x" 这样的前导系数或一元运算符 。
# 表达式按通常顺序进行求值：先是括号，然后求乘法，再计算加法和减法。
#
# 例如，expression = "1 + 2 * 3" 的答案是 ["7"]。
# 输出格式如下：
#
# 对于系数非零的每个自变量项，我们按字典排序的顺序将自变量写在一个项中。
# 例如，我们永远不会写像 “b*a*c” 这样的项，只写 “a*b*c”。
# 项的次数等于被乘的自变量的数目，并计算重复项。我们先写出答案的最大次数项，用字典顺序打破关系，此时忽略词的前导系数。
# 例如，"a*a*b*c" 的次数为 4。
# 项的前导系数直接放在左边，用星号将它与变量分隔开(如果存在的话)。前导系数 1 仍然要打印出来。
# 格式良好的一个示例答案是 ["-2*a*a*a", "3*a*a*b", "3*b*b", "4*a", "5*c", "-6"] 。
# 系数为 0 的项（包括常数项）不包括在内。
# 例如，“0” 的表达式输出为 [] 。
# 注意：你可以假设给定的表达式均有效。所有中间结果都在区间 [-231, 231 - 1] 内。
#
#
#
# 示例 1：
#
# 输入：expression = "e + 8 - a + 5", evalvars = ["e"], evalints = [1]
# 输出：["-1*a","14"]
# 示例 2：
#
# 输入：expression = "e - 8 + temperature - pressure",
# evalvars = ["e", "temperature"], evalints = [1, 12]
# 输出：["-1*pressure","5"]
# 示例 3：
#
# 输入：expression = "(e + 8) * (e - 8)", evalvars = [], evalints = []
# 输出：["1*e*e","-64"]
#
#
# 提示：
#
# 1 <= expression.length <= 250
# expression 由小写英文字母，数字 '+', '-', '*', '(', ')', ' ' 组成
# expression 不包含任何前空格或后空格
# expression 中的所有符号都用一个空格隔开
# 0 <= evalvars.length <= 100
# 1 <= evalvars[i].length <= 20
# evalvars[i] 由小写英文字母组成
# evalints.length == evalvars.length
# -100 <= evalints[i] <= 100

from leetcode.allcode.competition.mypackage import *

class Poly(Counter):
    def __add__(self, other):
        self.update(other)  # 不能直接相加，相加会自动丢弃<=0的结果
        return self

    def __sub__(self, other):
        self.update(Counter({k: -v for k, v in other.items()}))  # 不能直接相加，相加会自动丢弃<=0的结果
        return self

    def __mul__(self, other):
        res = Poly()
        for k1, v1 in self.items():
            for k2, v2 in other.items():
                res[tuple(sorted(k1 + k2))] += v1 * v2
        return res

    def eval(self, evalmap):  # 根据evalmap，把已知参数变成常数
        res = Poly()
        for k1, v1 in self.items():
            new_key = []
            for x in k1:
                if x in evalmap:
                    v1 *= evalmap[x]
                else:
                    new_key.append(x)
            res[tuple(new_key)] += v1   # key为空，表示常数项
        return res

    def to_list(self):  # 返回输出格式
        res = []
        for k, v in sorted(self.items(), key=lambda x: [-len(x[0]), x]):
            if v == 0: continue
            if len(k):
                e = str(v) + '*' + '*'.join(k)
            else:
                e = str(v)
            res.append(e)
        return res


class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:

        def combine(left, right, sign):
            if sign == '+':
                return left + right
            if sign == '-':
                return left - right
            return left * right

        def make(expr: str):
            ans = Poly()
            if expr.isdigit():
                ans[tuple()] = int(expr)
            else:
                ans[tuple([expr])] = 1
            return ans

        def parse(expr: str):
            polys = []
            signs = []
            n = len(expr)
            i = 0
            while i < n:
                if expr[i] == '(':
                    cnt = 1
                    for j in range(i + 1, n):
                        if expr[j] == '(':
                            cnt += 1
                        elif expr[j] == ')':
                            cnt -= 1
                            if cnt == 0:
                                polys.append(parse(expr[i + 1: j]))
                                i = j + 1
                                break
                elif expr[i].isalnum():
                    j = i
                    while j < n:
                        if expr[j] == ' ':
                            polys.append(make(expr[i: j]))
                            j += 1
                            break
                        j += 1
                    else:
                        polys.append(make(expr[i: j]))
                    i = j
                elif expr[i] in '+-*':
                    signs.append(expr[i])
                    i += 1
                else:
                    i += 1
            if len(polys) == 0:
                return Poly()

            i = 0
            while i < len(signs):
                if signs[i] == '*':  # 先进行乘法
                    polys[i] = combine(polys[i], polys[i + 1], signs[i])
                    polys.pop(i + 1)
                    signs.pop(i)
                    continue
                i += 1

            # 后进行加减法
            ans = polys[0]
            for i in range(len(signs)):
                ans = combine(ans, polys[i + 1], signs[i])
            return ans


        poly = parse(expression)
        evalmap = {a: b for a, b in zip(evalvars, evalints)}
        ans = poly.eval(evalmap)
        return ans.to_list()



so = Solution()
print(so.basicCalculatorIV(expression = "a * b * c + b * a * c * 4", evalvars = [], evalints = []))  # ["-1*pressure","5"]
print(so.basicCalculatorIV(expression = "e - 8 + temperature - pressure", evalvars = ["e", "temperature"], evalints = [1, 12]))  # ["-1*pressure","5"]
print(so.basicCalculatorIV(expression = "e + 8 - a + 5", evalvars = ["e"], evalints = [1]))  # ["-1*a","14"]

