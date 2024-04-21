# 找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：
#
# 只使用数字1到9
# 每个数字 最多使用一次
# 返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。
#
#
#
# 示例 1:
#
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
# 解释:
# 1 + 2 + 4 = 7
# 没有其他符合的组合了。
# 示例 2:
#
# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]
# 解释:
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# 没有其他符合的组合了。
# 示例 3:
#
# 输入: k = 4, n = 1
# 输出: []
# 解释: 不存在有效的组合。
# 在[1,9]范围内使用4个不同的数字，我们可以得到的最小和是1+2+3+4 = 10，因为10 > 1，没有有效的组合。
#
#
# 提示:
#
# 2 <= k <= 9
# 1 <= n <= 60

from leetcode.allcode.competition.mypackage import *

class Solution1:
    #允许超过9的组合解法
    def combinationSum3(self, k: int, n: int):
        l = self.A(k, n, 1)
        return l
    def A(self, k, n, lower_bound):
        #lower_bound，满足条件的组合各元素的下界
        if n == 2 or lower_bound > n:
            return []
        if n == 1:
            if k == 1:
                return [[1]]
            else:
                return []
        if k == 1:
            return [[n]]
        l = []
        for i in range(lower_bound, n):
            l_A = self.A(k-1, n-i, i+1)
            if len(l_A) > 0:
                for j in l_A:
                    j = j + [i]
                    l.append(j)
        return l
class Solution2:
    def combinationSum3(self, k: int, n: int):
        l = self.A(k, n, 1)
        return l
    def A(self, k, n, lower_bound):
        #lower_bound，满足条件的组合各元素的下界
        if n == 2 or lower_bound > n:
            return []
        if n == 1:
            if k == 1:
                return [[1]]
            return []
        if k == 1:
            if n > 9:
                return []
            return [[n]]
        l = []
        for i in range(lower_bound, n):
            l_A = self.A(k-1, n-i, i+1)
            if len(l_A) > 0:
                for j in l_A:
                    j = j + [i]
                    l.append(j)
        return l

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        @cache
        def dfs(start, num, target):
            if start > target or start > 9 or num == 0 or 10 - start < num:
                return []
            if start == target and num == 1:
                return [[start]]
            res = dfs(start + 1, num, target)
            l = dfs(start + 1, num - 1, target - start)
            for ll in l:
                res.append([start] + ll)
            return res

        return dfs(1, k, n)

so = Solution()
print(so.combinationSum3(4, 24))
print(so.combinationSum3(3, 9))
print(so.combinationSum3(2, 18))

