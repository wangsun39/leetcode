from typing import List

# 括号。设计一种算法，打印n对括号的所有合法的（例如，开闭一一对应）组合。
#
# 说明：解集不能包含重复的子集。
#
# 例如，给出 n = 3，生成结果为：
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = [[1, 1, '(']]  # res 中每个元素表示一个串，第一个元素表示这个串中有几个左括号，第二个元素表示左括号比右括号多几个，第三个元素是字符串
        for i in range(1, n * 2):
            temp = []
            for e in res:
                if n == e[0]:
                    e[1] -= 1
                    e[2] += ')'
                    continue
                if e[1] > 0:
                    temp.append([e[0] + 1, e[1] + 1, e[2] + '('])
                    e[1] -= 1
                    e[2] += ')'
                else:
                    e[0] += 1
                    e[1] += 1
                    e[2] += '('
            res += temp
        return [e[2] for e in res]


so = Solution()
print(so.generateParenthesis(3))




