# 给你一个二维整数数组 intervals ，其中 intervals[i] = [lefti, righti] 表示第 i 个区间开始于 lefti 、结束于 righti（包含两侧取值，闭区间）。区间的 长度 定义为区间中包含的整数数目，更正式地表达是 righti - lefti + 1 。
#
# 再给你一个整数数组 queries 。第 j 个查询的答案是满足 lefti <= queries[j] <= righti 的 长度最小区间 i 的长度 。如果不存在这样的区间，那么答案是 -1 。
#
# 以数组形式返回对应查询的所有答案。
#
#
#
# 示例 1：
#
# 输入：intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
# 输出：[3,3,1,4]
# 解释：查询处理如下：
# - Query = 2 ：区间 [2,4] 是包含 2 的最小区间，答案为 4 - 2 + 1 = 3 。
# - Query = 3 ：区间 [2,4] 是包含 3 的最小区间，答案为 4 - 2 + 1 = 3 。
# - Query = 4 ：区间 [4,4] 是包含 4 的最小区间，答案为 4 - 4 + 1 = 1 。
# - Query = 5 ：区间 [3,6] 是包含 5 的最小区间，答案为 6 - 3 + 1 = 4 。
# 示例 2：
#
# 输入：intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
# 输出：[2,-1,4,6]
# 解释：查询处理如下：
# - Query = 2 ：区间 [2,3] 是包含 2 的最小区间，答案为 3 - 2 + 1 = 2 。
# - Query = 19：不存在包含 19 的区间，答案为 -1 。
# - Query = 5 ：区间 [2,5] 是包含 5 的最小区间，答案为 5 - 2 + 1 = 4 。
# - Query = 22：区间 [20,25] 是包含 22 的最小区间，答案为 25 - 20 + 1 = 6 。
#
#
# 提示：
#
# 1 <= intervals.length <= 105
# 1 <= queries.length <= 105
# intervals[i].length == 2
# 1 <= lefti <= righti <= 107
# 1 <= queries[j] <= 107
from collections import deque
from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n = len(queries)
        ans = [-1] * n
        intervals.sort(key=lambda x: [x[1], x[0]])  # 按区间右端点+左端点排序
        # intervals.sort()  # 按区间右端点+左端点排序
        stack = deque()  # 记录区间长度的单调增栈
        cur = 0
        for i, q in sorted(enumerate(queries), key=lambda x: x[1]):
            # 先把 stack 中，右端点小于 q 的全部删除
            while stack and stack[0][1] < q:
                stack.popleft()
            while cur < len(intervals):
                # 将剩余的区间，能覆盖 q 的加入stack
                l, r = intervals[cur]
                # if q < l: break
                if r < q:
                    cur += 1
                    continue
                while stack and (stack[-1][1] - stack[-1][0] >= r - l):
                    stack.pop()
                stack.append([l, r])
                cur += 1
            if stack:
                # 剩下栈里的元素如果存在，一定都是能覆盖q的，那么最左侧的最小
                ans[i] = stack[0][1] - stack[0][0] + 1
        return ans

so = Solution()

print(so.minInterval([[4,5],[5,8],[1,9],[8,10],[1,6]], [7,9,3,9,3]))  # [4,3,6,3,6]
print(so.minInterval(intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]))  # [3,3,1,4]
print(so.minInterval(intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]))




