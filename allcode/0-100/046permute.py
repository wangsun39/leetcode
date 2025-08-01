# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 示例 2：
#
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
# 示例 3：
#
# 输入：nums = [1]
# 输出：[[1]]
#
#
# 提示：
#
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# nums 中的所有整数 互不相同

from leetcode.allcode.competition.mypackage import *

class Solution:
    def add_one_num(self, num, res):
        if len(res) == 0:
            res.append([num])
            return res
        m = len(res[0])
        new_res = []
        for one in res:
            for i in range(m+1):
                tmp = one[:]
                tmp.insert(i, num)
                new_res.append(tmp)
        return new_res
    def permute1(self, nums):
        res = []
        for i in nums:
            res = self.add_one_num(i, res)
        return res

    def permute(self, nums: List[int]) -> List[List[int]]:
        # 2025/8/1  换个写法
        n = len(nums)
        @cache
        def dfs(mask):
            if mask == 0:
                return [[]]
            res = []
            for i in range(n):
                if (1 << i) & mask:
                    arr = dfs(mask ^ (1 << i))
                    for y in arr:
                        res.append([nums[i]] + y)
            return res

        return dfs((1<<n)-1)


so = Solution()
print(so.permute([1,2,3,4]))
