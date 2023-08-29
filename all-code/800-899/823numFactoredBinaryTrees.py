# 给出一个含有不重复整数元素的数组 arr ，每个整数 arr[i] 均大于 1。
#
# 用这些整数来构建二叉树，每个整数可以使用任意次数。其中：每个非叶结点的值应等于它的两个子结点的值的乘积。
#
# 满足条件的二叉树一共有多少个？答案可能很大，返回 对 109 + 7 取余 的结果。
#
#
#
# 示例 1:
#
# 输入: arr = [2, 4]
# 输出: 3
# 解释: 可以得到这些二叉树: [2], [4], [4, 2, 2]
# 示例 2:
#
# 输入: arr = [2, 4, 5, 10]
# 输出: 7
# 解释: 可以得到这些二叉树: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].
#
#
# 提示：
#
# 1 <= arr.length <= 1000
# 2 <= arr[i] <= 109
# arr 中的所有值 互不相同

from math import inf
from typing import List
from functools import cache

class Solution:
    def numFactoredBinaryTrees1(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(arr)
        arr.sort()
        d = {x: i for i, x in enumerate(arr)}
        dp1 = [0] * n  # dp[i] 表示用前x个数，表示以 arr[i] 为根的二叉树总个数
        for i in range(n):
            dp1[i] += 1
            dp2 = [x for x in dp1]
            for j in range(n):
                if dp1[j] == 0: continue
                x = arr[j] * arr[i]
                if x in d:
                    if i != j:
                        dp2[d[x]] += dp1[j] * 2
                    else:
                        dp2[d[x]] += dp1[j]
                    dp2[d[x]] %= MOD
            dp1 = dp2
        return sum(dp1) % MOD

    def numFactoredBinaryTrees2(self, arr: List[int]) -> int:
        # 这种方式时不行的
        MOD = 10 ** 9 + 7
        s = set(arr)
        arr.sort()

        @cache
        def dfs(x):
            i = 2
            res = 1
            while i * i <= x:  # 这个地方x最大有10^9，因此可能超时
                if x % i == 0 and i in s:
                    j = x // i
                    if j in s:
                        if i * i == x:
                            res += dfs(i) ** 2
                        else:
                            res += dfs(i) * dfs(j) * 2
                    res %= MOD
                i += 1
            return res
        return sum(dfs(x) for x in s) % MOD


    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(arr)
        s = set(arr)
        arr.sort()

        @cache
        def dfs(x):
            res = 1
            for i in range(n):
                if arr[i] * arr[i] > x: break
                if x % arr[i] == 0:
                    y = x // arr[i]
                    if y in s:
                        if arr[i] == y:
                            res += dfs(arr[i]) ** 2
                        else:
                            res += dfs(arr[i]) * dfs(y) * 2
                    res %= MOD
            return res
        return sum(dfs(x) for x in s) % MOD



so = Solution()
print(so.numFactoredBinaryTrees([2, 4]))  # 3
print(so.numFactoredBinaryTrees([18,3,6,2]))  # 12
print(so.numFactoredBinaryTrees(arr = [2, 4, 5, 10]))  # 7

