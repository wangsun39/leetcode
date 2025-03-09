# 给你一个二维整数数组 items ，其中 items[i] = [pricei, beautyi] 分别表示每一个物品的 价格 和 美丽值 。
#
# 同时给你一个下标从 0 开始的整数数组 queries 。对于每个查询 queries[j] ，你想求出价格小于等于 queries[j] 的物品中，最大的美丽值 是多少。如果不存在符合条件的物品，那么查询的结果为 0 。
#
# 请你返回一个长度与 queries 相同的数组 answer，其中 answer[j]是第 j 个查询的答案。
#
#
#
# 示例 1：
#
# 输入：items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]
# 输出：[2,4,5,5,6,6]
# 解释：
# - queries[0]=1 ，[1,2] 是唯一价格 <= 1 的物品。所以这个查询的答案为 2 。
# - queries[1]=2 ，符合条件的物品有 [1,2] 和 [2,4] 。
#   它们中的最大美丽值为 4 。
# - queries[2]=3 和 queries[3]=4 ，符合条件的物品都为 [1,2] ，[3,2] ，[2,4] 和 [3,5] 。
#   它们中的最大美丽值为 5 。
# - queries[4]=5 和 queries[5]=6 ，所有物品都符合条件。
#   所以，答案为所有物品中的最大美丽值，为 6 。
# 示例 2：
#
# 输入：items = [[1,2],[1,2],[1,3],[1,4]], queries = [1]
# 输出：[4]
# 解释：
# 每个物品的价格均为 1 ，所以我们选择最大美丽值 4 。
# 注意，多个物品可能有相同的价格和美丽值。
# 示例 3：
#
# 输入：items = [[10,1000]], queries = [5]
# 输出：[0]
# 解释：
# 没有物品的价格小于等于 5 ，所以没有物品可以选择。
# 因此，查询的结果为 0 。
#
#
# 提示：
#
# 1 <= items.length, queries.length <= 105
# items[i].length == 2
# 1 <= pricei, beautyi, queries[j] <= 109

from leetcode.allcode.competition.mypackage import *

class Solution1:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        mx = 0
        n = len(items)
        cur = 0
        ans = [0] * len(queries)
        for i, limit in sorted(enumerate(queries), key=lambda x:x[1]):
            while cur < n and items[cur][0] <= limit:
                mx = max(mx, items[cur][1])
                cur += 1
            ans[i] = mx
        return ans

class Fenwick2:
    # 求前缀最大值（区间求max不能用!!!）
    # 所有函数参数下标从1开始，可以传入使用者的数值x+1的值
    __slots__ = ['f', 'nums']

    def __init__(self, n: int):
        # n 是能调用下面函数的下标最大值
        self.f = [0] * (n + 1)   # 关键区间最大值

    def update(self, i: int, val: int) -> None:  # nums[i] = val
        while i < len(self.f):
            self.f[i] = max(self.f[i], val)
            i += i & -i

    def query(self, i: int) -> int:  # 下标<=i的最大值
        mx = 0
        while i > 0:
            mx = max(mx, self.f[i])
            i &= i - 1
        return mx

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        idx = list(set(x for x, _ in items) | set(queries))
        n = len(idx)
        fw = Fenwick2(n)
        idx.sort()
        map = {x: i + 1 for i, x in enumerate(idx)}
        for x, y in items:
            fw.update(map[x], y)
        return [fw.query(map[x]) for x in queries]


so = Solution()
print(so.maximumBeauty(items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]))
print(so.maximumBeauty(items = [[1,2],[1,2],[1,3],[1,4]], queries = [1]))
print(so.maximumBeauty(items = [[10,1000]], queries = [5]))


