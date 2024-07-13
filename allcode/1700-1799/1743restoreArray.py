# 存在一个由 n 个不同元素组成的整数数组 nums ，但你已经记不清具体内容。好在你还记得 nums 中的每一对相邻元素。
#
# 给你一个二维整数数组 adjacentPairs ，大小为 n - 1 ，其中每个 adjacentPairs[i] = [ui, vi] 表示元素 ui 和 vi 在 nums 中相邻。
#
# 题目数据保证所有由元素 nums[i] 和 nums[i+1] 组成的相邻元素对都存在于 adjacentPairs 中，存在形式可能是 [nums[i], nums[i+1]] ，也可能是 [nums[i+1], nums[i]] 。这些相邻元素对可以 按任意顺序 出现。
#
# 返回 原始数组 nums 。如果存在多种解答，返回 其中任意一个 即可。
#
#
#
# 示例 1：
#
# 输入：adjacentPairs = [[2,1],[3,4],[3,2]]
# 输出：[1,2,3,4]
# 解释：数组的所有相邻元素对都在 adjacentPairs 中。
# 特别要注意的是，adjacentPairs[i] 只表示两个元素相邻，并不保证其 左-右 顺序。
# 示例 2：
#
# 输入：adjacentPairs = [[4,-2],[1,4],[-3,1]]
# 输出：[-2,4,1,-3]
# 解释：数组中可能存在负数。
# 另一种解答是 [-3,1,4,-2] ，也会被视作正确答案。
# 示例 3：
#
# 输入：adjacentPairs = [[100000,-100000]]
# 输出：[100000,-100000]
#
#
# 提示：
#
# nums.length == n
# adjacentPairs.length == n - 1
# adjacentPairs[i].length == 2
# 2 <= n <= 105
# -105 <= nums[i], ui, vi <= 105
# 题目数据保证存在一些以 adjacentPairs 作为元素对的数组 nums

from leetcode.allcode.competition.mypackage import *

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # 考虑重复元素的情况，实际题目要求没有重复
        g = defaultdict(Counter)
        for x, y in adjacentPairs:
            g[x][y] += 1
            g[y][x] += 1
        start = end = None
        for x in g:
            if sum(g[x].values()) & 1:
                if start is None:
                    start = x
                else:
                    end = x
                    break
        if start is None:
            start = end = 1
        x = start
        ans = []
        while True:
            ans.append(x)
            y = list(g[x].keys())[0]
            if y == end and list(g[y].values())[0] == 1:
                if len(g[x]) == 1:
                    ans.append(y)
                    return ans
                continue
            g[x][y] -= 1
            if g[x][y] == 0:
                del(g[x][y])
            g[y][x] -= 1
            if g[y][x] == 0:
                del(g[y][x])
            x = y

so = Solution()
print(so.restoreArray([[2,1],[3,4],[3,2]]))
print(so.restoreArray(adjacentPairs = [[4,-2],[1,4],[-3,1]]))
print(so.restoreArray(adjacentPairs = [[100000,-100000]]))
