# 有些数的素因子只有 3，5，7，请设计一个算法找出第 k 个数。注意，不是必须有这些素因子，而是必须不包含其他的素因子。例如，前几个数按顺序应该是 1，3，5，7，9，15，21。
#
# 示例 1:
#
# 输入: k = 5
#
# 输出: 9
#
# https://leetcode.cn/problems/get-kth-magic-number-lcci



from typing import List
from collections import defaultdict
from functools import lru_cache
import heapq

class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        queue = [1]
        s = set([1])
        for _ in range(k):
            x = heapq.heappop(queue)
            if x * 3 not in s:
                heapq.heappush(queue, x * 3)
                s.add(x * 3)
            if x * 5 not in s:
                heapq.heappush(queue, x * 5)
                s.add(x * 5)
            if x * 7 not in s:
                heapq.heappush(queue, x * 7)
                s.add(x * 7)
        return x





so = Solution()
print(so.getKthMagicNumber(5))




