# 对于字符串 s 和 t，只有在 s = t + t + t + ... + t + t（t 自身连接 1 次或多次）时，我们才认定 “t 能除尽 s”。
#
# 给定两个字符串 str1 和 str2 。返回 最长字符串 x，要求满足 x 能除尽 str1 且 x 能除尽 str2 。
#
#
#
# 示例 1：
#
# 输入：str1 = "ABCABC", str2 = "ABC"
# 输出："ABC"
# 示例 2：
#
# 输入：str1 = "ABABAB", str2 = "ABAB"
# 输出："AB"
# 示例 3：
#
# 输入：str1 = "LEET", str2 = "CODE"
# 输出：""
#
#
# 提示：
#
# 1 <= str1.length, str2.length <= 1000
# str1 和 str2 由大写英文字母组成
import math

from leetcode.allcode.competition.mypackage import *

class Solution:
    def get_gcd(self, n1, n2):
        if n1 == n2:
            return n1
        if n1 < n2:
            n1, n2 = n2, n1
        while n1 % n2 != 0:
            n1 %= n2
            n1, n2 = n2, n1
        return n2
    def gcdOfStrings1(self, str1: str, str2: str):
        def isDividedBy(a, b):
            length = len(a)
            for i in range(len(b)//length):
                if a != b[i*length:i*length+length]:
                    return False
            return True
        len1, len2 = len(str1), len(str2)
        if 0 == len1 or 0 == len2:
            return ''
        greatest_common_divisor = self.get_gcd(len1, len2)
        print(greatest_common_divisor)
        for i in range(greatest_common_divisor, 0, -1):
            if isDividedBy(str1[:greatest_common_divisor], str1) and isDividedBy(str1[:greatest_common_divisor], str2):
                return str1[:greatest_common_divisor]
        return ''

    def gcdOfStrings(self, str1: str, str2: str):
        # 2024/5/18 用库函数
        n1, n2 = len(str1), len(str2)
        g = math.gcd(n1, n2)
        for i in range(g, 0, -1):
            if n1 % i or n2 % i: continue
            core = str1[:i]
            if any(core != str1[j * i: i * (j + 1)] for j in range(n1 // i)):
                continue
            if any(core != str2[j * i: i * (j + 1)] for j in range(n2 // i)):
                continue
            return core
        return ''


obj = Solution()
print(obj.gcdOfStrings('ABCABC','ABC'))
print(obj.gcdOfStrings(str1 = "ABABAB", str2 = "ABAB"))

