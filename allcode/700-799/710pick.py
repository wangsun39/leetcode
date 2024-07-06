# 给定一个整数 n 和一个 无重复 黑名单整数数组 blacklist 。设计一种算法，从 [0, n - 1] 范围内的任意整数中选取一个 未加入 黑名单 blacklist 的整数。任何在上述范围内且不在黑名单 blacklist 中的整数都应该有 同等的可能性 被返回。
#
# 优化你的算法，使它最小化调用语言 内置 随机函数的次数。
#
# 实现 Solution 类:
#
# Solution(int n, int[] blacklist) 初始化整数 n 和被加入黑名单 blacklist 的整数
# int pick() 返回一个范围为 [0, n - 1] 且不在黑名单 blacklist 中的随机整数
#  
#
# 示例 1：
#
# 输入
# ["Solution", "pick", "pick", "pick", "pick", "pick", "pick", "pick"]
# [[7, [2, 3, 5]], [], [], [], [], [], [], []]
# 输出
# [null, 0, 4, 1, 6, 1, 0, 4]
#
# 解释
# Solution solution = new Solution(7, [2, 3, 5]);
# solution.pick(); // 返回0，任何[0,1,4,6]的整数都可以。注意，对于每一个pick的调用，
#                  // 0、1、4和6的返回概率必须相等(即概率为1/4)。
# solution.pick(); // 返回 4
# solution.pick(); // 返回 1
# solution.pick(); // 返回 6
# solution.pick(); // 返回 1
# solution.pick(); // 返回 0
# solution.pick(); // 返回 4
#  
#
# 提示:
#
# 1 <= n <= 109
# 0 <= blacklist.length <= min(105, n - 1)
# 0 <= blacklist[i] < n
# blacklist 中所有值都 不同
#  pick 最多被调用 2 * 104 次



from leetcode.allcode.competition.mypackage import *

class Solution1:

    def __init__(self, n: int, blacklist: List[int]):
        self.n = n - len(blacklist)
        m = len(blacklist)
        self.d = {}
        j = n - m
        for i in range(m):
            if blacklist[i] >= n - m:
                continue
            while j in blacklist:
                j += 1
            self.d[blacklist[i]] = j
            j += 1

    def pick(self) -> int:
        ans = random.randrange(0, self.n)
        if ans in self.d:
            return self.d[ans]
        return ans

class Solution:
    # 2024/7/5 二分法

    def __init__(self, n: int, blacklist: List[int]):
        self.n = n
        self.m = len(blacklist)
        blacklist.sort()
        self.blacklist = blacklist


    def pick(self) -> int:
        num = random.randrange(0, self.n - self.m)
        def check(v):  # 检查区间[0,v]中是否有num个数
            p = bisect_right(self.blacklist, v)  # <= v的blacklist数字个数
            return v - p >= num
        if check(0): return 0
        lo, hi = 0, self.n
        while lo < hi - 1:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid
        return hi





# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()

so = Solution(4, [2,1])
print(so.pick())
print(so.pick())
print(so.pick())
print(so.pick())



