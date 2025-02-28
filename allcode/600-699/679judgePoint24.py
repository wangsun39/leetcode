# 给定一个长度为4的整数数组 cards 。你有 4 张卡片，每张卡片上都包含一个范围在 [1,9] 的数字。您应该使用运算符 ['+', '-', '*', '/'] 和括号 '(' 和 ')' 将这些卡片上的数字排列成数学表达式，以获得值24。
#
# 你须遵守以下规则:
#
# 除法运算符 '/' 表示实数除法，而不是整数除法。
# 例如， 4 /(1 - 2 / 3)= 4 /(1 / 3)= 12 。
# 每个运算都在两个数字之间。特别是，不能使用 “-” 作为一元运算符。
# 例如，如果 cards =[1,1,1,1] ，则表达式 “-1 -1 -1 -1” 是 不允许 的。
# 你不能把数字串在一起
# 例如，如果 cards =[1,2,1,2] ，则表达式 “12 + 12” 无效。
# 如果可以得到这样的表达式，其计算结果为 24 ，则返回 true ，否则返回 false 。
#
#
#
# 示例 1:
#
# 输入: cards = [4, 1, 8, 7]
# 输出: true
# 解释: (8-4) * (7-1) = 24
# 示例 2:
#
# 输入: cards = [1, 2, 1, 2]
# 输出: false
#
#
# 提示:
#
# cards.length == 4
# 1 <= cards[i] <= 9

from leetcode.allcode.competition.mypackage import *

p2 = list(product(['+', '-', '*', '/'], repeat=3))  # 生成 3 个范围为 0-3 的序列
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        p1 = list(permutations(cards))  # 迭代器必须转成list，否则只能使用一次
        @cache
        def calc(x, s, y):
            if s == '+': return x + y
            if s == '-': return x - y
            if s == '*': return x * y
            return x / y if y else 99999
        for a, b, c, d in p1: # (a + b) + (c + d)
            for x, y, z in p2:
                if abs(calc(calc(a, x, b), y, calc(c, z, d)) - 24) < 0.0000001: return True
        for a, b, c, d in p1: # (((a + b) + c) + d)
            for x, y, z in p2:
                if abs(calc(calc(calc(a, x, b), y, c), z, d) - 24) < 0.0000001: return True
        for a, b, c, d in p1: # a + (b + (c + d))
            for x, y, z in p2:
                if abs(calc(a, x, calc(b, y, calc(c, z, d))) - 24) < 0.0000001: return True
        for a, b, c, d in p1: # a + ((b + c) + d))
            for x, y, z in p2:
                if abs(calc(a, x, calc(calc(b, y, c), z, d)) - 24) < 0.0000001: return True
        for a, b, c, d in p1: # (a + (b + c)) + d
            for x, y, z in p2:
                if abs(calc(calc(a, x, calc(b, y, c)), z, d) - 24) < 0.0000001: return True
        return False




obj = Solution()
print(obj.judgePoint24([1, 4, 5, 6]))   # 4 / (1 - (5 / 6))
print(obj.judgePoint24([1, 5, 5, 5]))
print(obj.judgePoint24([3, 3, 8, 8]))
print(obj.judgePoint24([4, 1, 8, 7]))
print(obj.judgePoint24([1, 2, 1, 2]))