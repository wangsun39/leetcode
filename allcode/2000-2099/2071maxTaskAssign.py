# 给你 n 个任务和 m 个工人。每个任务需要一定的力量值才能完成，需要的力量值保存在下标从 0 开始的整数数组 tasks 中，第 i 个任务需要 tasks[i] 的力量才能完成。每个工人的力量值保存在下标从 0 开始的整数数组 workers 中，第 j 个工人的力量值为 workers[j] 。每个工人只能完成 一个 任务，且力量值需要 大于等于 该任务的力量要求值（即 workers[j] >= tasks[i] ）。
#
# 除此以外，你还有 pills 个神奇药丸，可以给 一个工人的力量值 增加 strength 。你可以决定给哪些工人使用药丸，但每个工人 最多 只能使用 一片 药丸。
#
# 给你下标从 0 开始的整数数组tasks 和 workers 以及两个整数 pills 和 strength ，请你返回 最多 有多少个任务可以被完成。
#
#
#
# 示例 1：
#
# 输入：tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1
# 输出：3
# 解释：
# 我们可以按照如下方案安排药丸：
# - 给 0 号工人药丸。
# - 0 号工人完成任务 2（0 + 1 >= 1）
# - 1 号工人完成任务 1（3 >= 2）
# - 2 号工人完成任务 0（3 >= 3）
# 示例 2：
#
# 输入：tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5
# 输出：1
# 解释：
# 我们可以按照如下方案安排药丸：
# - 给 0 号工人药丸。
# - 0 号工人完成任务 0（0 + 5 >= 5）
# 示例 3：
#
# 输入：tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10
# 输出：2
# 解释：
# 我们可以按照如下方案安排药丸：
# - 给 0 号和 1 号工人药丸。
# - 0 号工人完成任务 0（0 + 10 >= 10）
# - 1 号工人完成任务 1（10 + 10 >= 15）
# 示例 4：
#
# 输入：tasks = [5,9,8,5,9], workers = [1,6,4,2,6], pills = 1, strength = 5
# 输出：3
# 解释：
# 我们可以按照如下方案安排药丸：
# - 给 2 号工人药丸。
# - 1 号工人完成任务 0（6 >= 5）
# - 2 号工人完成任务 2（4 + 5 >= 8）
# - 4 号工人完成任务 3（6 >= 5）
#
#
# 提示：
#
# n == tasks.length
# m == workers.length
# 1 <= n, m <= 5 * 104
# 0 <= pills <= m
# 0 <= tasks[i], workers[j], strength <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        n, m = len(tasks), len(workers)
        tasks.sort()
        workers.sort()

        def check(val):
            # 是否能完成val个任务
            if val > m: return False
            cnt = 0  # 使用的药数量
            hp1 = workers[-val:]
            # hp1 = [[x, 0] for x in hp]   # 0 表示这个x是没有使用药丸
            heapify(hp1)  # 表示没有使用药丸
            hp2 = []
            for i in range(val):
                if hp1 and hp2:
                    if hp1[0] < hp2[0]:

                if hp1 and hp1[0] >= tasks[i]:
                    x = heappop(hp1)
                    continue
                if hp1 and hp1[0]
                    heappush(hp2, x + strength)

                if hp2 and hp2[0] >= tasks[i]:
                    heappop(hp2)
                    continue
                if cnt < pills and hp1 and hp1[0] + strength >= tasks[i]:
                    heappop(hp1)
                    cnt += 1
                else:
                    return False
            return True
        lo, hi = 0, n + 1
        while lo < hi - 1:
            mid = (lo + hi) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid
        return lo


so = Solution()
print(so.maxTaskAssign(tasks = [5,9,8,5,9], workers = [1,6,4,2,6], pills = 1, strength = 5))  # 3
print(so.maxTaskAssign(tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10))  # 2
print(so.maxTaskAssign(tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1))  # 3
print(so.maxTaskAssign(tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5))  # 1




