# 给定一个仅包含数字 0-9 的字符串 num 和一个目标值整数 target ，在 num 的数字之间添加 二元 运算符（不是一元）+、- 或 * ，返回 所有 能够得到 target 的表达式。
#
# 注意，返回表达式中的操作数 不应该 包含前导零。
#
#
#
# 示例 1:
#
# 输入: num = "123", target = 6
# 输出: ["1+2+3", "1*2*3"]
# 解释: “1*2*3” 和 “1+2+3” 的值都是6。
# 示例 2:
#
# 输入: num = "232", target = 8
# 输出: ["2*3+2", "2+3*2"]
# 解释: “2*3+2” 和 “2+3*2” 的值都是8。
# 示例 3:
#
# 输入: num = "3456237490", target = 9191
# 输出: []
# 解释: 表达式 “3456237490” 无法得到 9191 。
#
#
# 提示：
#
# 1 <= num.length <= 10
# num 仅含数字
# -231 <= target <= 231 - 1

from leetcode.allcode.competition.mypackage import *

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        num = list(num)
        d = {0: '', 1: '+', 2: '-', 3: '*'}  # 四进制表示
        ans = []
        @cache
        def evaluate(s: str):
            if s.isdigit(): return int(s)
            m = len(s)
            for i in range(m - 1, -1, -1):
                x = s[i]
                if x == '+':
                    return evaluate(s[:i]) + evaluate(s[i + 1:])
                elif x == '-':
                    return evaluate(s[:i]) - evaluate(s[i + 1:])

            p1 = s.rfind('*')
            return evaluate(s[:p1]) * evaluate(s[p1 + 1:])

        evaluate("1-23+45-67+89")

        for i in range(4 ** (n - 1)):
            # 取出i 的4进制表示中的每个位
            sign = []
            fail = False
            for _ in range(n - 1):
                j = i % 4
                sign.append(d[j])
                i //= 4
            res = [num[0]]
            for j in range(n - 1):
                if j == 0 and res[0] == '0' and sign[j] == '':
                    fail = True
                    break
                res.append(sign[j])
                if num[j + 1] == '0' and j != n - 2 and sign[j] != '' == sign[j + 1]:
                    fail = True
                    break
                res.append(num[j + 1])
            if fail: continue
            expr = ''.join(res)
            # print(expr)
            if evaluate(expr) != eval(expr) == target:
                print(expr)
            if evaluate(expr) == target:
                ans.append(expr)
        return ans


so = Solution()
print(so.addOperators(num = "123456789", target = 45))
print(so.addOperators(num = "232", target = 8))
print(so.addOperators(num = "00", target = 0))
print(so.addOperators(num = "105", target = 5))
print(so.addOperators(num = "123", target = 6))