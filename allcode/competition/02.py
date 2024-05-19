

from leetcode.allcode.competition.mypackage import *

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        d = []  # 记录所有下标i，其中nums[i]和nums[i+1]奇偶性相同
        for i in range(n - 1):
            if (nums[i] + nums[i + 1]) & 1 == 0:
                d.append(i)
        ans = []
        for x, y in queries:
            if x == y:
                ans.append(True)
                continue
            px = bisect_right(d, x)
            py = bisect_right(d, y - 1)
            if py <= 0 or (px == py and d[px - 1] != x):
                ans.append(True)
            else:
                ans.append(False)
        return ans


so = Solution()
print(so.isArraySpecial([4,1,2,9,9,8,8], [[1,5]]))
print(so.isArraySpecial(nums = [3,4,1,2,6], queries = [[0,4]]))
print(so.isArraySpecial(nums = [4,3,1,6], queries = [[0,2],[2,3]]))




