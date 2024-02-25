

from leetcode.allcode.competition.mypackage import *

class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        n = len(nums)
        m = len(changeIndices)
        s = sum(nums)

        def check(t):  # 检查时间t内是否能完成
            left = s
            vis = set()
            for i in range(t, 0, -1):
                idx = changeIndices[i - 1] - 1
                if idx not in vis:
                    v = nums[idx]
                    left -= v
                    vis.add(idx)
                if left + n - len(vis) > i - 1: return False
            return left == 0 and len(vis) == n

        for i in range(s + n, m + 1):
            if check(i):
                return i
        return -1


so = Solution()
print(so.earliestSecondToMarkIndices([1,0,1,2], [3,1,1,4,4,4,4,2,2,1,3,4]))  # 11
print(so.earliestSecondToMarkIndices(nums = [2,2,0], changeIndices = [2,2,2,2,3,2,2,1]))
print(so.earliestSecondToMarkIndices(nums = [1,3], changeIndices = [1,1,1,2,1,1,1]))
print(so.earliestSecondToMarkIndices(nums = [0,1], changeIndices = [2,2,2]))




