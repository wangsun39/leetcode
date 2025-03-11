# 给你一个整数数组 nums ，找出并返回所有该数组中不同的递增子序列，递增子序列中 至少有两个元素 。你可以按 任意顺序 返回答案。
#
# 数组中可能含有重复元素，如出现两个整数相等，也可以视作递增序列的一种特殊情况。
#
#
#
# 示例 1：
#
# 输入：nums = [4,6,7,7]
# 输出：[[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
# 示例 2：
#
# 输入：nums = [4,4,3,2,1]
# 输出：[[4,4]]
#
#
# 提示：
#
# 1 <= nums.length <= 15
# -100 <= nums[i] <= 100


from leetcode.allcode.competition.mypackage import *

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        def dfs(start):
            if start == n: return [[]]
            arrs = dfs(start + 1)
            res = []
            for arr in arrs:
                if len(arr) == 0 or nums[start] <= arr[0]:
                    res.append([nums[start]] + arr)
            return arrs + res

        ans = dfs(0)
        ans = [tuple(x) for x in ans if len(x) >= 2]
        ans = list(set(ans))
        return [list(x) for x in ans]



so = Solution()
print(so.findSubsequences([4,6,7,7]))

