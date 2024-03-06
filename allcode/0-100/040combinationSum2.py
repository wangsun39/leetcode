# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的每个数字在每个组合中只能使用 一次 。
#
# 注意：解集不能包含重复的组合。
#
#
#
# 示例 1:
#
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# 示例 2:
#
# 输入: candidates = [2,5,2,1,2], target = 5,
# 输出:
# [
# [1,2,2],
# [5]
# ]
#
#
# 提示:
#
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30

from leetcode.allcode.competition.mypackage import *

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        counter = Counter(candidates)
        counter = [[k, v] for k, v in counter.items() if k <= target]
        n = len(counter)

        def dfs(start, t):
            if t == 0:
                return [[]]
            res = []
            for i in range(start, n):
                k, v = counter[i]
                if v > 0 and k <= t:
                    counter[i][1] -= 1
                    r = dfs(i, t - k)
                    for rr in r:
                        res.append([k] + rr)
                    counter[i][1] += 1
            return res

        return dfs(0, target)


so = Solution()
print(so.combinationSum2(candidates = [5,4,5,1,5,3,1,4,5,5,4], target = 10))
print(so.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))
print(so.combinationSum2(candidates = [2,5,2,1,2], target = 5))




