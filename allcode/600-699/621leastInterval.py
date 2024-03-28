# 给你一个用字符数组 tasks 表示的 CPU 需要执行的任务列表，用字母 A 到 Z 表示，以及一个冷却时间 n。每个周期或时间间隔允许完成一项任务。任务可以按任何顺序完成，但有一个限制：两个 相同种类 的任务之间必须有长度为 n 的冷却时间。
#
# 返回完成所有任务所需要的 最短时间间隔 。
#
#
#
# 示例 1：
#
# 输入：tasks = ["A","A","A","B","B","B"], n = 2
# 输出：8
# 解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B
#      在本示例中，两个相同类型任务之间必须间隔长度为 n = 2 的冷却时间，而执行一个任务只需要一个单位时间，所以中间出现了（待命）状态。
# 示例 2：
#
# 输入：tasks = ["A","A","A","B","B","B"], n = 0
# 输出：6
# 解释：在这种情况下，任何大小为 6 的排列都可以满足要求，因为 n = 0
# ["A","A","A","B","B","B"]
# ["A","B","A","B","A","B"]
# ["B","B","B","A","A","A"]
# ...
# 诸如此类
# 示例 3：
#
# 输入：tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
# 输出：16
# 解释：一种可能的解决方案是：
#      A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> (待命) -> (待命) -> A -> (待命) -> (待命) -> A
#
#
# 提示：
#
# 1 <= tasks.length <= 104
# tasks[i] 是大写英文字母
# 0 <= n <= 100

from leetcode.allcode.competition.mypackage import *

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        m = len(tasks)
        counter = Counter(tasks)
        mx = max(counter.values())  # 最大的出现次数
        n_key = list(counter.values()).count(mx)  # 出现最大次数的字母个数

        # if m - mx >= n * mx:
        if m - mx * n_key >= (mx - 1) * (n + 1 - n_key):
            # 考虑这样的执行顺序
            # 宽度就是 n + 1
            # A B C D
            # A B C D
            # A B E F
            # A B E G
            return m
        else:
            # 考虑这样的执行顺序
            # 宽度就是 n + 1，除了最后一行，其他空位就是要待命的时间
            # A B C D
            # A B C D
            # A B E F
            # A B G
            # 不足格子的各填充 1 个待命的时间
            return m + ((mx - 1) * (n + 1 - n_key) - (m - mx * n_key))


so = Solution()
print(so.leastInterval(tasks = ["A","A","A","B","B","B"], n = 2))  # 8
print(so.leastInterval(tasks = ["A","B","C","D","A","B","V"], n = 3))
print(so.leastInterval(tasks = ["A","B","A","B"], n = 2))   # 5
print(so.leastInterval(tasks = ["A","A","A","B","B","B"], n = 0))  # 6
print(so.leastInterval(tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2))  # 16




