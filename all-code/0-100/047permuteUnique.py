# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
#
#
#
# 示例 1：
#
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# 示例 2：
#
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#
# 提示：
#
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10
from collections import Counter
from typing import List


# 两数之和
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        counter = [[x, c] for x, c in counter.items()]

        def dfs(ct):
            res = []
            for i, [k, v] in enumerate(ct):
                if v != 0:
                    ct[i][1] -= 1
                    l = dfs(ct)
                    if len(l) == 0:
                        res += [[k]]
                    else:
                        res += [[k] + ll for ll in l]
                    ct[i][1] += 1
            return res

        return dfs(counter)





so = Solution()
print(so.permuteUnique([1,1,2]))
print(so.permuteUnique([1,2,3]))
