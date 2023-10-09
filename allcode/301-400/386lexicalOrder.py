# 给你一个整数 n ，按字典序返回范围 [1, n] 内所有整数。
#
# 你必须设计一个时间复杂度为 O(n) 且使用 O(1) 额外空间的算法。
#
#  
#
# 示例 1：
#
# 输入：n = 13
# 输出：[1,10,11,12,13,2,3,4,5,6,7,8,9]
# 示例 2：
#
# 输入：n = 2
# 输出：[1,2]
#  
#
# 提示：
#
# 1 <= n <= 5 * 104



from collections import defaultdict
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        cur = 1
        ans = [cur]
        while True:
            next = cur * 10
            if next <= n:
                cur = next
                ans.append(cur)
                continue

            if cur % 10 == 9:
                next = cur // 10 + 1
                if str(next) <= str(cur):
                    break
                cur = next
                ans.append(cur)
                continue
            next = cur + 1
            if next <= n:
                cur = next
                ans.append(cur)
                continue
            next = cur // 10 + 1
            if str(next) <= str(cur):
                break
            cur = next
            ans.append(cur)
            continue
        return ans



so = Solution()
print(so.lexicalOrder(99))
print(so.lexicalOrder(13))
print(so.lexicalOrder(2))

