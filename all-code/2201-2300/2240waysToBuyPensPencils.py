


from typing import List
from collections import deque
# Definition for a binary tree node.
from collections import Counter
class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ans = 0
        for i in range(total + 1):
            if total < i * cost1:
                break
            ans += ((total - i * cost1) // cost2 + 1)
        return ans


so = Solution()


