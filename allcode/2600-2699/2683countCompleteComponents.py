# 下标从 0 开始、长度为 n 的数组 derived 是由同样长度为 n 的原始 二进制数组 original 通过计算相邻值的 按位异或（⊕）派生而来。
#
# 特别地，对于范围 [0, n - 1] 内的每个下标 i ：
#
# 如果 i = n - 1 ，那么 derived[i] = original[i] ⊕ original[0]
# 否则 derived[i] = original[i] ⊕ original[i + 1]
# 给你一个数组 derived ，请判断是否存在一个能够派生得到 derived 的 有效原始二进制数组 original 。
#
# 如果存在满足要求的原始二进制数组，返回 true ；否则，返回 false 。
#
# 二进制数组是仅由 0 和 1 组成的数组。
#
#
# 示例 1：
#
# 输入：derived = [1,1,0]
# 输出：true
# 解释：能够派生得到 [1,1,0] 的有效原始二进制数组是 [0,1,0] ：
# derived[0] = original[0] ⊕ original[1] = 0 ⊕ 1 = 1
# derived[1] = original[1] ⊕ original[2] = 1 ⊕ 0 = 1
# derived[2] = original[2] ⊕ original[0] = 0 ⊕ 0 = 0
# 示例 2：
#
# 输入：derived = [1,1]
# 输出：true
# 解释：能够派生得到 [1,1] 的有效原始二进制数组是 [0,1] ：
# derived[0] = original[0] ⊕ original[1] = 1
# derived[1] = original[1] ⊕ original[0] = 1
# 示例 3：
#
# 输入：derived = [1,0]
# 输出：false
# 解释：不存在能够派生得到 [1,0] 的有效原始二进制数组。
#
#
# 提示：
#
# n == derived.length
# 1 <= n <= 105
# derived 中的值不是 0 就是 1 。
from leetcode.allcode.competition.mypackage import *


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        fa = list(range(n))
        def find(x):
            if x != fa[x]:
                fa[x] = find(fa[x])
            return fa[x]

        def union(x, y):
            fa[find(y)] = find(x)

        for x, y in edges:
            union(x, y)
        for i in range(n):
            find(i)
        # print(fa)
        counter = Counter(fa)
        edges_nums = defaultdict(int)
        for x, y in edges:
            edges_nums[fa[x]] += 1
        ans = 0
        for k, v in counter.items():
            if v * (v - 1) // 2 == edges_nums[k]:
                ans += 1
        return ans


so = Solution()
print(so.countCompleteComponents(n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]))
print(so.countCompleteComponents(n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]))




