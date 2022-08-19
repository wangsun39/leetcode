# 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
#
#  
#
# 示例 1：
#
# 输入：n = 13
# 输出：6
# 示例 2：
#
# 输入：n = 0
# 输出：0
#  
#
# 提示：
#
# 0 <= n <= 109
from functools import lru_cache

class Solution:
    def countDigitOne(self, n: int) -> int:
        oneNum = [i * pow(10, i - 1) for i in range(10)]  # oneNum[i] 表示小于i+1位数的数中有多少个1，比如 oneNum[1] 小于2位数的所有数有几个1
        # print(oneNum)
        string = str(n)
        length = len(string)
        res = 0
        for i in range(length):
            digit = int(string[i])
            ds = length - i  # 表示当前数字是第几位数
            if digit == 1:
                if i + 1 == length:  # 最后一位
                    res += 1
                else:
                    res += int(string[i + 1:]) + 1 + oneNum[ds - 1] # 比如 1200，int(string[i + 1:])表示1000-1200在千位上有201个1，oneNum[ds - 1]表示[0,999]有多个1
            elif digit == 0:
                continue
            else:
                res += oneNum[ds - 1] * digit + pow(10, ds - 1)
            # print(res)
        return int(res)

    def countDigitOne1(self, n: int) -> int:  # 用数位模板的解法
        s = str(n)
        @lru_cache(None)
        def helper(i: int, is_limit: bool) -> int:  # 返回值，从第i位开始向右的部分，考虑is_limit的场景，共有多少个1
            if i == len(s):
                return 0
            ans = 0
            upper = int(s[i]) if is_limit else 9  # 判断当前位是否受约束
            for j in range(upper + 1):
                ans += helper(i + 1, is_limit and j == upper)
                if j == 1:
                    if i == len(s) - 1:
                        ans += 1
                    elif j != upper:
                        ans += (10 ** (len(s) - i - 1))
                    else:
                        ans += (int(s[i + 1:]) + 1)
            return ans
        return helper(0, True)





so = Solution()
print(so.countDigitOne1(11))   # 4
print(so.countDigitOne1(13))  # 6
print(so.countDigitOne1(10))  # 2
print(so.countDigitOne1(0))   # 0



