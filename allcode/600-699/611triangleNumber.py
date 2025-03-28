# 给定一个包含非负整数的数组 nums ，返回其中可以组成三角形三条边的三元组个数。
#
#
#
# 示例 1:
#
# 输入: nums = [2,2,3,4]
# 输出: 3
# 解释:有效的组合是:
# 2,3,4 (使用第一个 2)
# 2,3,4 (使用第二个 2)
# 2,2,3
# 示例 2:
#
# 输入: nums = [4,2,3,4]
# 输出: 4
#
#
# 提示:
#
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000

from leetcode.allcode.competition.mypackage import *

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        nums = [x for x in nums if x]
        n = len(nums)
        if n <= 2: return 0
        dq = deque(nums[1:])
        l1 = [nums[0]]
        ans = 0
        for _ in range(n - 1):
            x = dq.popleft()
            for y in l1:
                p1 = bisect_right(dq,y-x)
                p2 = bisect_left(dq,y+x)
                ans += p2 - p1
            l1.append(x)
        return ans

so = Solution()
print(so.triangleNumber([0,0,0]))
print(so.triangleNumber([2,2,3,4]))

