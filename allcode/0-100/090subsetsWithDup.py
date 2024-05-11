# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的 子集（幂集）。
#
# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
# 示例 2：
#
# 输入：nums = [0]
# 输出：[[],[0]]
#
#
# 提示：
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10

from leetcode.allcode.competition.mypackage import *

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        counter = [[k, v] for k, v in counter.items()]

        def dfs(i):
            # 前i种数的所以子集
            if i < 0:
                return [[]]
            k, v = counter[i]
            ans = []
            for j in range(v + 1):
                res = dfs(i - 1)
                for l in res:
                    ans.append([k] * j + l)
            return ans
        return dfs(len(counter) - 1)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        counter = [[k, v] for k, v in counter.items()]

        def dfs(i):
            # 前i种数的所以子集
            if i < 0:
                return [[]]
            k, v = counter[i]
            if v == 0:
            ans = []
            for j in range(v + 1):
                res = dfs(i - 1)
                for l in res:
                    ans.append([k] * j + l)
            return ans
        return dfs(len(counter) - 1)



so = Solution()
print(so.subsetsWithDup([1,2,2]))




