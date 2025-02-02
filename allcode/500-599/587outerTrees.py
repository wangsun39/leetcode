# 在一个二维的花园中，有一些用 (x, y) 坐标表示的树。由于安装费用十分昂贵，你的任务是先用最短的绳子围起所有的树。只有当所有的树都被绳子包围时，花园才能围好栅栏。你需要找到正好位于栅栏边界上的树的坐标。
#
#
#
# 示例 1:
#
# 输入: [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
# 输出: [[1,1],[2,0],[4,2],[3,3],[2,4]]
# 解释:
#
# 示例 2:
#
# 输入: [[1,2],[2,2],[4,2]]
# 输出: [[1,2],[2,2],[4,2]]
# 解释:
#
# 即使树都在一条直线上，你也需要先用绳子包围它们。
#
#
# 注意:
#
# 所有的树应当被围在一起。你不能剪断绳子来包围树或者把树分成一组以上。
# 输入的整数在 0 到 100 之间。
# 花园至少有一棵树。
# 所有树的坐标都是不同的。
# 输入的点没有顺序。输出顺序也没有要求。


from leetcode.allcode.competition.mypackage import *


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        maxScope = 101
        barrels = [[] for _ in range(maxScope)]
        for tree in trees:
            barrels[tree[0]].append(tree[1])
        for bar in barrels:
            bar.sort(reverse=True)
        print(barrels)
        for i in range(maxScope):
            if len(barrels[i]) > 0:
                minX = i
                break
        for i in range(maxScope - 1, -1, -1):
            if len(barrels[i]) > 0:
                maxX = i
                break
        if minX == maxX:
            return trees
        ans = [[minX, i] for i in barrels[minX]] + [[maxX, i] for i in barrels[maxX]]
        print(ans)
        def findMaxSlopeFrom(start): # 从与start连接的斜率最大的一个点的坐标
            slope = -100000  # 斜率
            x = -1
            for i in range(start[0] + 1, maxScope):
                if len(barrels[i]) > 0 and (barrels[i][0] - start[1])/(i - start[0]) > slope:
                    slope = (barrels[i][0] - start[1])/(i - start[0])
                    x = i
            return [x, barrels[x][0]]
        def findMinSlopeFrom(start): # 从与start连接的斜率最小的一个点的坐标
            slope = 100000  # 斜率
            x = -1
            for i in range(start[0] + 1, maxScope):
                if len(barrels[i]) > 0 and (barrels[i][-1] - start[1])/(i - start[0]) < slope:
                    slope = (barrels[i][-1] - start[1])/(i - start[0])
                    x = i
            return [x, barrels[x][-1]]
        def find():
            start = [minX, barrels[minX][0]]
            while True:
                start = findMaxSlopeFrom(start)
                if start[0] >= maxX:
                    break
                if start not in ans:
                    ans.append(start)
            start = [minX, barrels[minX][-1]]
            while True:
                start = findMinSlopeFrom(start)
                if start[0] >= maxX:
                    break
                if start not in ans:
                    ans.append(start)

        find()
        return ans


so = Solution()
print(so.outerTrees([[0,0],[1,1],[100,100]]))
print(so.outerTrees([[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]))
print(so.outerTrees([[1,2],[2,2],[4,2]]))
