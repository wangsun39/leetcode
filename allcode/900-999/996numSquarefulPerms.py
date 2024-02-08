# 给定一个非负整数数组 A，如果该数组每对相邻元素之和是一个完全平方数，则称这一数组为正方形数组。
#
# 返回 A 的正方形排列的数目。两个排列 A1 和 A2 不同的充要条件是存在某个索引 i，使得 A1[i] != A2[i]。
#
#
#
# 示例 1：
#
# 输入：[1,17,8]
# 输出：2
# 解释：
# [1,8,17] 和 [17,8,1] 都是有效的排列。
# 示例 2：
#
# 输入：[2,2,2]
# 输出：1
#
#
# 提示：
#
# 1 <= A.length <= 12
# 0 <= A[i] <= 1e9

from leetcode.allcode.competition.mypackage import *

class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def square(x):
            return int(x ** 0.5) ** 2 == x
        counter = Counter(nums)
        counter = [[k, v] for k, v in counter.items()]
        d = {}
        for i, [k, v] in enumerate(counter):
            d[k] = i  # num在counter数组中的下标

        @cache
        def dfs(start, bits):
            res = 0
            l = list(bits)
            if sum(bits) == 0:
                return 1
            for num in d.keys():
                if l[d[num]] and (square(num + start) or start == -1):
                    l[d[num]] -= 1
                    res += dfs(num, tuple(l))
                    l[d[num]] += 1
            return res
        return dfs(-1, tuple(v for _, v in counter))






so = Solution()
print(so.numSquarefulPerms([1,17,8]))
print(so.numSquarefulPerms([2,2,2]))




