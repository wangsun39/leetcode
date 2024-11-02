
# Map = [['U' for _ in range(n)] for _ in range(m)]

from typing import List
from collections import deque
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# d = defaultdict(int)


import bisect
# bisect_right：
# 若序列a中存在与x相同的元素，则返回x相等元素右侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x左侧距离最近元素插入点的索引位置
# pos = bisect.bisect_right(left, tail)
# bisect_left：
# 若序列a中存在与x相同的元素，则返回x相等元素左侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x右侧距离最近元素插入点的索引位置

from functools import lru_cache
from typing import List
# @lru_cache(None)

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort(key=lambda x:x[0])
        n = len(stockPrices)
        if n <= 2:
            return n - 1
        start, cur = 0, 2
        ans = 1
        print(stockPrices)
        def equal(A, B, C):
            return (B[1] - A[1]) * (C[0] - B[0]) == (C[1] - B[1]) * (B[0] - A[0])
        while cur < n:
            if equal(stockPrices[start], stockPrices[start + 1], stockPrices[cur]):
                cur += 1
                continue
            start = cur - 1
            cur = cur + 1
            ans += 1
        return ans


so = Solution()
print(so.minimumLines([[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]]))
print(so.minimumLines([[3,4],[1,2],[7,8],[2,3]]))




