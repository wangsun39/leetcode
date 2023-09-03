# 给你一个正整数 n ，请你找出符合条件的最小整数，其由重新排列 n 中存在的每位数字组成，并且其值大于 n 。如果不存在这样的正整数，则返回 -1 。
#
# 注意 ，返回的整数应当是一个 32 位整数 ，如果存在满足题意的答案，但不是 32 位整数 ，同样返回 -1 。
#
#  
#
# 示例 1：
#
# 输入：n = 12
# 输出：21
# 示例 2：
#
# 输入：n = 21
# 输出：-1
#  
#
# 提示：
#
# 1 <= n <= 231 - 1


from typing import List
from collections import defaultdict
import bisect

class Solution:
    def nextGreaterElement1(self, n: int) -> int:
        digits = []
        cur = n
        while cur > 0:
            digits.insert(0, cur % 10)
            cur = cur // 10
        print(digits)
        N = len(digits)
        i = N - 2
        while i >= 0:
            if digits[i] < digits[i + 1]:
                break
            i -= 1
        if i < 0:
            return -1
        j = i + 1
        while j < N:
            if digits[j] <= digits[i]:
                break
            j += 1
        digits[i], digits[j - 1] = digits[j - 1], digits[i]
        digits = digits[:i + 1] + digits[i + 1:][::-1]
        res = digits[0]
        for e in digits[1:]:
            res *= 10
            res += e
        return res if res <= 2147483647 else -1

    def nextGreaterElement(self, n: int) -> int:  # 20220703
        stack = []
        s = str(n)
        m = len(s)
        for i in range(m - 1, -1, -1):
            if len(stack) == 0 or s[i] >= stack[-1]:
                stack.append(s[i])
            else:
                head = s[:i]
                j = bisect.bisect_right(stack, s[i])
                mid = stack[j]
                stack[j] = s[i]
                ans = int(head + mid + ''.join(stack))
                return -1 if ans > int(2 ** 31 - 1) else ans
        return -1


so = Solution()
print(so.nextGreaterElement(12443322))
print(so.nextGreaterElement(2147483486))
print(so.nextGreaterElement(21))
print(so.nextGreaterElement(12))
print(so.nextGreaterElement(1234506))

