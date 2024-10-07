# 几乎每一个人都用 乘法表。但是你能在乘法表中快速找到第k小的数字吗？
#
# 给定高度m 、宽度n 的一张 m * n的乘法表，以及正整数k，你需要返回表中第k 小的数字。
#
# 例 1：
#
# 输入: m = 3, n = 3, k = 5
# 输出: 3
# 解释:
# 乘法表:
# 1	2	3
# 2	4	6
# 3	6	9
#
# 第5小的数字是 3 (1, 2, 2, 3, 3).
# 例 2：
#
# 输入: m = 2, n = 3, k = 6
# 输出: 6
# 解释:
# 乘法表:
# 1	2	3
# 2	4	6
#
# 第6小的数字是 6 (1, 2, 2, 3, 4, 6).
# 注意：
#
# m 和 n 的范围在 [1, 30000] 之间。
# k 的范围在 [1, m * n] 之间。



from leetcode.allcode.competition.mypackage import *

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        if m > n:
            m, n = n, m
        def getRanking(k):  # 判断数字k在表中排第几，next是在乘法表中第k小的数
            ans = 0
            next = 1e9
            for i in range(1, m + 1):
                if k % i == 0:
                    num = k // i - 1
                else:
                    num = k // i
                ans += min(num, n)
                if num < n:
                    next = min((num + 1) * i, next)
            return ans + 1, next

        start, end = 1, k
        cur = (start + end) // 2
        pre = 1
        while start <= end:
            ranking, next = getRanking(cur)
            if ranking == k:
                return next
            if ranking < k:
                start = cur + 1
                pre = next
            else:
                end = cur - 1
            cur = (start + end) // 2
        return next if ranking < k else pre



so = Solution()


print(so.findKthNumber(m = 2, n = 3, k = 6))  # 6
print(so.findKthNumber(m = 3, n = 3, k = 6))  # 4
print(so.findKthNumber(m = 3, n = 3, k = 5))  # 3
print(so.findKthNumber(m = 3, n = 3, k = 1))  # 1
print(so.findKthNumber(m = 3, n = 3, k = 2))  # 2

