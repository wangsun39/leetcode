# 给你一个长度为 n ，下标从 0 开始的整数数组 forts ，表示一些城堡。forts[i] 可以是 -1 ，0 或者 1 ，其中：
#
# -1 表示第 i 个位置 没有 城堡。
# 0 表示第 i 个位置有一个 敌人 的城堡。
# 1 表示第 i 个位置有一个你控制的城堡。
# 现在，你需要决定，将你的军队从某个你控制的城堡位置 i 移动到一个空的位置 j ，满足：
#
# 0 <= i, j <= n - 1
# 军队经过的位置 只有 敌人的城堡。正式的，对于所有 min(i,j) < k < max(i,j) 的 k ，都满足 forts[k] == 0 。
# 当军队移动时，所有途中经过的敌人城堡都会被 摧毁 。
#
# 请你返回 最多 可以摧毁的敌人城堡数目。如果 无法 移动你的军队，或者没有你控制的城堡，请返回 0 。
#
#
#
# 示例 1：
#
# 输入：forts = [1,0,0,-1,0,0,0,0,1]
# 输出：4
# 解释：
# - 将军队从位置 0 移动到位置 3 ，摧毁 2 个敌人城堡，位置分别在 1 和 2 。
# - 将军队从位置 8 移动到位置 3 ，摧毁 4 个敌人城堡。
# 4 是最多可以摧毁的敌人城堡数目，所以我们返回 4 。
# 示例 2：
#
# 输入：forts = [0,0,1,-1]
# 输出：0
# 解释：由于无法摧毁敌人的城堡，所以返回 0 。
#
#
# 提示：
#
# 1 <= forts.length <= 1000
# -1 <= forts[i] <= 1

from leetcode.allcode.competition.mypackage import *

class Solution:
    def captureForts1(self, forts: List[int]) -> int:
        n = len(forts)
        ans = 0
        def f(l):
            nonlocal ans
            for i in range(n):
                if l[i] != 1: continue
                j = i + 1
                while j < n and l[j] == 0:
                    j += 1
                if j < n and l[j] == -1:
                    ans = max(ans, j - i - 1)
        f(forts)
        f(forts[::-1])
        return ans

    def captureForts(self, forts: List[int]) -> int:
        # update 2023/9/2
        n = len(forts)
        def f(l):  # 找 1,0,-1
            ans = 0
            i = 0
            while i < n:
                if l[i] != 1:
                    i += 1
                    continue
                j = i + 1
                while j < n and l[j] == 0:
                    j += 1
                if j < n and l[j] == -1:
                    ans = max(ans, j - i - 1)
                i = j
            return ans
        return max(f(forts), f(forts[::-1]))




so = Solution()
print(so.captureForts(forts = [-1,0,1,0,0,0]))
print(so.captureForts(forts = [1,0,0,-1,0,0,0,0,1]))
print(so.captureForts(forts = [0,0,1,-1]))




