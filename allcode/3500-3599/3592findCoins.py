# 给你一个 从 1 开始计数 的整数数组 numWays，其中 numWays[i] 表示使用某些 固定 面值的硬币（每种面值可以使用无限次）凑出总金额 i 的方法数。每种面值都是一个 正整数 ，并且其值 最多 为 numWays.length。
#
# 然而，具体的硬币面值已经 丢失 。你的任务是还原出可能生成这个 numWays 数组的面值集合。
#
# 返回一个按从小到大顺序排列的数组，其中包含所有可能的 唯一 整数面值。
#
# 如果不存在这样的集合，返回一个 空 数组。
#
#
#
# 示例 1：
#
# 输入： numWays = [0,1,0,2,0,3,0,4,0,5]
#
# 输出： [2,4,6]
#
# 解释：
#
# 金额	方法数	解释
# 1	0	无法用硬币凑出总金额 1。
# 2	1	唯一的方法是 [2]。
# 3	0	无法用硬币凑出总金额 3。
# 4	2	可以用 [2, 2] 或 [4]。
# 5	0	无法用硬币凑出总金额 5。
# 6	3	可以用 [2, 2, 2]、[2, 4] 或 [6]。
# 7	0	无法用硬币凑出总金额 7。
# 8	4	可以用 [2, 2, 2, 2]、[2, 2, 4]、[2, 6] 或 [4, 4]。
# 9	0	无法用硬币凑出总金额 9。
# 10	5	可以用 [2, 2, 2, 2, 2]、[2, 2, 2, 4]、[2, 4, 4]、[2, 2, 6] 或 [4, 6]。
# 示例 2：
#
# 输入： numWays = [1,2,2,3,4]
#
# 输出： [1,2,5]
#
# 解释：
#
# 金额	方法数	解释
# 1	1	唯一的方法是 [1]。
# 2	2	可以用 [1, 1] 或 [2]。
# 3	2	可以用 [1, 1, 1] 或 [1, 2]。
# 4	3	可以用 [1, 1, 1, 1]、[1, 1, 2] 或 [2, 2]。
# 5	4	可以用 [1, 1, 1, 1, 1]、[1, 1, 1, 2]、[1, 2, 2] 或 [5]。
# 示例 3：
#
# 输入： numWays = [1,2,3,4,15]
#
# 输出： []
#
# 解释：
#
# 没有任何面值集合可以生成该数组。
#
#
#
# 提示：
#
# 1 <= numWays.length <= 100
# 0 <= numWays[i] <= 2 * 108

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        arr = []
        s = set()

        def calc(val):
            n = len(arr)
            if n == 0: return 0

            @cache
            def dfs(idx, t):
                if t == 0: return 1
                if idx == 0:
                    return 1 if t % arr[0] == 0 else 0
                res = 0
                i = 0
                while arr[idx] * i <= t:
                    res += dfs(idx - 1, t - arr[idx] * i)
                    i += 1
                return res
            return dfs(n - 1, val)

        for i, x in enumerate(numWays, 1):
            num = calc(i)
            if num == x - 1:
                arr.append(i)
                s.add(i)
            elif num == x:
                pass
            else:
                return []

        return arr



so = Solution()
print(so.findCoins([1,2,3,4,15]))
print(so.findCoins([0,1,0,2,0,3,0,4,0,5]))




