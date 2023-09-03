# 给定一个整数 n ，你需要找到与它最近的回文数（不包括自身）。
#
# “最近的”定义为两个整数差的绝对值最小。
#
# 示例 1:
#
# 输入: "123"
# 输出: "121"
# 注意:
#
# n 是由字符串表示的正整数，其长度不超过18。
# 如果有多个结果，返回最小的那个。



from typing import List
from collections import defaultdict


class Solution:
    def nearestPalindromic1(self, n: str) -> str:
        N = len(n)
        halfLen = N // 2
        firstHalf = n[:halfLen]
        # secondHalf = n[halfLen:]
        if N % 2 == 0:
            new1 = firstHalf + firstHalf[::-1]
            if new1 == n:
                new1 = None
            # mid = int(firstHalf[-1])
            firstHalfNum = int(firstHalf)
            if len(str(firstHalfNum + 1)) > halfLen:
                new2 = str(firstHalfNum + 1) + str(firstHalfNum + 1)[::-1][1:]
            else:
                new2 = str(firstHalfNum + 1) + str(firstHalfNum + 1)[::-1]
            if 0 == firstHalfNum - 1:
                new3 = '9'
            elif len(str(firstHalfNum - 1)) < halfLen:
                new3 = str(firstHalfNum - 1) + '9' + str(firstHalfNum - 1)[::-1]
            else:
                new3 = str(firstHalfNum - 1) + str(firstHalfNum - 1)[::-1]
        else:
            mid = int(n[halfLen])
            new1 = firstHalf + str(mid) + firstHalf[::-1]
            if new1 == n:
                new1 = None
            firstHalfNum = int(firstHalf + n[halfLen])
            if len(str(firstHalfNum + 1)) > halfLen + 1:
                new2 = str(firstHalfNum + 1) + str(firstHalfNum + 1)[::-1][2:]
            else:
                new2 = str(firstHalfNum + 1) + str(firstHalfNum + 1)[::-1][1:]
            if len(str(firstHalfNum - 1)) < halfLen + 1:
                new3 = str(firstHalfNum - 1) + str(firstHalfNum - 1)[::-1]
            else:
                new3 = str(firstHalfNum - 1) + str(firstHalfNum - 1)[::-1][1:]

        def selectNew(s1, s2):
            if s1 is None:
                return s2
            if s2 is None:
                return s1
            d1, d2 = abs(int(s1) - int(n)), abs(int(s2) - int(n))
            if d1 == d2:
                return s1
            return s1 if d1 < d2 else s2
        print(new1, new2, new3)
        res = selectNew(new1, new2)
        res = selectNew(new3, res)
        return res

    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        if length == 1:
            return n
        halfLen = length // 2
        halfNum1 = int(n[:halfLen])
        halfNum2, halfNum3 = halfNum1 + 1, halfNum1 - 1
        if len(n) % 2 == 0:
            new1 = str(halfNum1) + str(halfNum1)[::-1]
            new2 = str(halfNum2) + str(halfNum2)[::-1]
            new3 = str(halfNum3) + str(halfNum3)[::-1]
        else:
            new1 = str(halfNum1) + n[halfLen] + str(halfNum1)[::-1]
            new2 = str(halfNum2) + n[halfLen] + str(halfNum2)[::-1]
            new3 = str(halfNum3) + n[halfLen] + str(halfNum3)[::-1]
        delta1, delta2, delta3 = abs(int(new1) - int(n)), abs(int(new2) - int(n)), abs(int(new3) - int(n))
        if delta3 <= delta2 and delta3 <= delta1:
            return new3
        if delta1 <= delta2 and delta1 < delta3:
            return new1
        return new2



so = Solution()
print(so.nearestPalindromic("6"))
print(so.nearestPalindromic("11"))
print(so.nearestPalindromic("10"))
print(so.nearestPalindromic("11067"))
print(so.nearestPalindromic("10067"))
print(so.nearestPalindromic("99167"))
print(so.nearestPalindromic("99967"))
print(so.nearestPalindromic("199867"))
print(so.nearestPalindromic("9986"))
print(so.nearestPalindromic("12453638"))

