# 给你两个整数数组 source 和 target ，长度都是 n 。还有一个数组 allowedSwaps ，其中每个 allowedSwaps[i] = [ai, bi] 表示你可以交换数组 source 中下标为 ai 和 bi（下标从 0 开始）的两个元素。注意，你可以按 任意 顺序 多次 交换一对特定下标指向的元素。
#
# 相同长度的两个数组 source 和 target 间的 汉明距离 是元素不同的下标数量。形式上，其值等于满足 source[i] != target[i] （下标从 0 开始）的下标 i（0 <= i <= n-1）的数量。
#
# 在对数组 source 执行 任意 数量的交换操作后，返回 source 和 target 间的 最小汉明距离 。
#
#
#
# 示例 1：
#
# 输入：source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]
# 输出：1
# 解释：source 可以按下述方式转换：
# - 交换下标 0 和 1 指向的元素：source = [2,1,3,4]
# - 交换下标 2 和 3 指向的元素：source = [2,1,4,3]
# source 和 target 间的汉明距离是 1 ，二者有 1 处元素不同，在下标 3 。
# 示例 2：
#
# 输入：source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []
# 输出：2
# 解释：不能对 source 执行交换操作。
# source 和 target 间的汉明距离是 2 ，二者有 2 处元素不同，在下标 1 和下标 2 。
# 示例 3：
#
# 输入：source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]
# 输出：0
#
#
# 提示：
#
# n == source.length == target.length
# 1 <= n <= 105
# 1 <= source[i], target[i] <= 105
# 0 <= allowedSwaps.length <= 105
# allowedSwaps[i].length == 2
# 0 <= ai, bi <= n - 1
# ai != bi

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        fa = list(range(n))
        # fa = {x: x for x in nums}  # 另一种写法，x不连续
        def find(x):
            if x != fa[x]:
                fa[x] = find(fa[x])
            return fa[x]
        def union(x, y):
            fa[find(y)] = find(x)

        for x, y in allowedSwaps:
            union(x, y)
        for i in range(n):
            find(i)
        d = defaultdict(list)  # d[i] 记录并查集代表元素是i的所有下标
        for i, x in enumerate(fa):
            d[x].append(i)
        ans = 0
        for l in d.values():
            ss = Counter([source[x] for x in l])
            tt = Counter([target[x] for x in l])
            for k, v in ss.items():
                if k in tt:
                    ss[k] -= min(v, tt[k])
            ans += sum(ss.values())
        return ans


so = Solution()
print(so.minimumHammingDistance([50,46,54,35,18,42,26,72,75,47,50,4,54,21,18,18,61,64,100,14],
[83,34,43,73,61,94,10,68,74,31,54,46,28,60,18,18,4,44,79,92],
[[1,8],[14,17],[3,1],[17,10],[18,2],[7,12],[11,3],[1,15],[13,17],[18,19],[0,10],[15,19],[0,15],[6,7],[7,15],[19,4],[7,16],[14,18],[8,10],[17,0],[2,13],[14,10],[12,17],[2,9],[6,15],[16,18],[2,16],[2,6],[4,5],[17,5],[10,13],[7,2],[9,16],[15,5],[0,5],[8,0],[11,12],[9,7],[1,0],[11,17],[4,6],[5,7],[19,12],[3,18],[19,1],[13,18],[19,6],[13,6],[6,1],[4,2]]))
print(so.minimumHammingDistance(source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]))
print(so.minimumHammingDistance(source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []))
print(so.minimumHammingDistance(source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]))




