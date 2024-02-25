

from leetcode.allcode.competition.mypackage import *

class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        n = len(nums)
        m = len(changeIndices)
        s = sum(nums)

        def check(t):  # 检查时间t内是否能完成
            nums2 = nums[:]
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
print(so.earliestSecondToMarkIndices(nums = [3,2,3], changeIndices = [1,3,2,2,2,2,3]))




