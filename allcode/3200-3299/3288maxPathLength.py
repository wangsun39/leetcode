# 给你一个长度为 n 的二维整数数组 coordinates 和一个整数 k ，其中 0 <= k < n 。
#
# coordinates[i] = [xi, yi] 表示二维平面里一个点 (xi, yi) 。
#
# 如果一个点序列 (x1, y1), (x2, y2), (x3, y3), ..., (xm, ym) 满足以下条件，那么我们称它是一个长度为 m 的 上升序列 ：
#
# 对于所有满足 1 <= i < m 的 i 都有 xi < xi + 1 且 yi < yi + 1 。
# 对于所有 1 <= i <= m 的 i 对应的点 (xi, yi) 都在给定的坐标数组里。
# 请你返回包含坐标 coordinates[k] 的 最长上升路径 的长度。
#
#
#
# 示例 1：
#
# 输入：coordinates = [[3,1],[2,2],[4,1],[0,0],[5,3]], k = 1
#
# 输出：3
#
# 解释：
#
# (0, 0) ，(2, 2) ，(5, 3) 是包含坐标 (2, 2) 的最长上升路径。
#
# 示例 2：
#
# 输入：coordinates = [[2,1],[7,0],[5,6]], k = 2
#
# 输出：2
#
# 解释：
#
# (2, 1) ，(5, 6) 是包含坐标 (5, 6) 的最长上升路径。
#
#
#
# 提示：
#
# 1 <= n == coordinates.length <= 105
# coordinates[i].length == 2
# 0 <= coordinates[i][0], coordinates[i][1] <= 109
# coordinates 中的元素 互不相同 。
# 0 <= k <= n - 1

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:
        x0, y0 = coordinates[k]
        dd1 = defaultdict(list)
        dd2 = defaultdict(list)
        for x, y in coordinates:
            if x < x0 and y < y0:
                dd1[x].append(y)
            elif x > x0 and y > y0:
                dd2[x].append(y)
        coo1 = sorted(dd1.items())  # x坐标比 k 小的点
        coo1 = [v for _, v in coo1]
        coo2 = sorted(dd2.items())  # x坐标比 k 大的点
        coo2 = [v for _, v in coo2]

        def proc(coo):
            for v in coo:
                v.sort()
            stack = [coo[0][0]]  # stack[i] 表示长度为i + 1的序列，末尾最小值
            for l in coo[1:]:
                mx_stack = stack[-1]
                for x in l:
                    if x > mx_stack:
                        stack.append(x)
                        break
                    if x == mx_stack: continue
                    p = bisect_left(stack, x)
                    if p == len(stack): continue
                    if stack[p] > x:
                        stack[p] = x
            return len(stack)
        ans = 1
        if coo1:
            ans += proc(coo1)
        if coo2:
            ans += proc(coo2)
        return ans



so = Solution()
print(so.maxPathLength(coordinates = [[4,8],[8,8],[2,9],[2,1],[9,6],[3,7],[8,4],[3,4],[7,8]], k = 3))  # 3
print(so.maxPathLength(coordinates = [[3,5],[1,4],[2,0],[9,9],[6,5],[2,2]], k = 0))  # 3
print(so.maxPathLength(coordinates = [[4,8],[1,3],[1,6],[5,8],[2,1],[2,4],[7,6]], k = 0))  # 3
print(so.maxPathLength(coordinates = [[9,5],[1,4],[1,7],[9,8],[6,4],[6,7]], k = 3))  # 3
print(so.maxPathLength(coordinates = [[0,1],[4,5],[2,9],[1,4],[8,8],[8,9]], k = 3))  # 4
print(so.maxPathLength(coordinates = [[0,1],[1,0],[8,4],[3,6],[4,6],[9,7],[4,8]], k = 1))  # 3
print(so.maxPathLength(coordinates = [[8,4],[8,9],[5,2],[2,4],[3,2],[3,1]], k = 0))  # 3
print(so.maxPathLength(coordinates = [[0,3],[8,5],[6,8]], k = 0))
print(so.maxPathLength(coordinates = [[2,1],[7,0],[5,6]], k = 2))
print(so.maxPathLength(coordinates = [[3,1],[2,2],[4,1],[0,0],[5,3]], k = 1))




