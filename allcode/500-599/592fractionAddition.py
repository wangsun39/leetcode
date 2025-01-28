# 给定一个表示分数加减运算的字符串expression，你需要返回一个字符串形式的计算结果。
#
# 这个结果应该是不可约分的分数，即最简分数。如果最终结果是一个整数，例如2，你需要将它转换成分数形式，其分母为1。所以在上述例子中, 2应该被转换为2/1。
#
# 
#
# 示例1:
#
# 输入:expression= "-1/2+1/2"
# 输出: "0/1"
# 示例 2:
#
# 输入:expression= "-1/2+1/2+1/3"
# 输出: "1/3"
# 示例 3:
#
# 输入:expression= "1/3-1/2"
# 输出: "-1/6"
# 
#
# 提示:
#
# 输入和输出字符串只包含'0' 到'9'的数字，以及'/', '+' 和'-'。
# 输入和输出分数格式均为±分子/分母。如果输入的第一个分数或者输出的分数是正数，则'+'会被省略掉。
# 输入只包含合法的最简分数，每个分数的分子与分母的范围是[1,10]。如果分母是1，意味着这个分数实际上是一个整数。
# 输入的分数个数范围是 [1,10]。
# 最终结果的分子与分母保证是 32 位整数范围内的有效整数。




from typing import List
import collections

import math

class Solution:
    def fractionAddition(self, expression: str) -> str:
        def oper(a, b, sign):
            [a1, a2] = a.split('/')
            [b1, b2] = b.split('/')
            a1, a2, b1, b2 = int(a1), int(a2), int(b1), int(b2)
            if sign == '+':
                c1 = a1 * b2 + a2 * b1
                c2 = a2 * b2
            else:
                c1 = a1 * b2 - a2 * b1
                c2 = a2 * b2
            c = math.gcd(c1, c2)
            c1 //= c
            c2 //= c
            return str(c1) + '/' + str(c2)

        if expression[0] == '-':
            expression = '0/1' + expression
        nums = []
        signs = []
        i, j = 0, 1
        while j < len(expression):
            if expression[j] in ('+-'):
                nums.append(expression[i:j])
                signs.append(expression[j])
                j += 1
                i = j
            j += 1
        nums.append(expression[i:])
        print(nums)
        print(signs)
        n = len(nums)
        ans = nums[0]
        for i in range(1, n):
            ans = oper(ans, nums[i], signs[i - 1])
            print(ans)
        return ans

so = Solution()

print('ret = ', so.fractionAddition("-1/2+1/2"))
print('ret = ', so.fractionAddition("-1/2+1/2+1/3"))
print('ret = ', so.fractionAddition("1/3-1/2"))

