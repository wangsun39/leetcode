# 一个音乐会总共有 n 排座位，编号从 0 到 n - 1 ，每一排有 m 个座椅，编号为 0 到 m - 1 。你需要设计一个买票系统，针对以下情况进行座位安排：
#
# 同一组的 k 位观众坐在 同一排座位，且座位连续 。
# k 位观众中 每一位 都有座位坐，但他们 不一定 坐在一起。
# 由于观众非常挑剔，所以：
#
# 只有当一个组里所有成员座位的排数都 小于等于 maxRow ，这个组才能订座位。每一组的 maxRow 可能 不同 。
# 如果有多排座位可以选择，优先选择 最小 的排数。如果同一排中有多个座位可以坐，优先选择号码 最小 的。
# 请你实现 BookMyShow 类：
#
# BookMyShow(int n, int m) ，初始化对象，n 是排数，m 是每一排的座位数。
# int[] gather(int k, int maxRow) 返回长度为 2 的数组，表示 k 个成员中 第一个座位 的排数和座位编号，这 k 位成员必须坐在 同一排座位，且座位连续 。换言之，返回最小可能的 r 和 c 满足第 r 排中 [c, c + k - 1] 的座位都是空的，且 r <= maxRow 。如果 无法 安排座位，返回 [] 。
# boolean scatter(int k, int maxRow) 如果组里所有 k 个成员 不一定 要坐在一起的前提下，都能在第 0 排到第 maxRow 排之间找到座位，那么请返回 true 。这种情况下，每个成员都优先找排数 最小 ，然后是座位编号最小的座位。如果不能安排所有 k 个成员的座位，请返回 false 。
#  
#
# 示例 1：
#
# 输入：
# ["BookMyShow", "gather", "gather", "scatter", "scatter"]
# [[2, 5], [4, 0], [2, 0], [5, 1], [5, 1]]
# 输出：
# [null, [0, 0], [], true, false]
#
# 解释：
# BookMyShow bms = new BookMyShow(2, 5); // 总共有 2 排，每排 5 个座位。
# bms.gather(4, 0); // 返回 [0, 0]
#                   // 这一组安排第 0 排 [0, 3] 的座位。
# bms.gather(2, 0); // 返回 []
#                   // 第 0 排只剩下 1 个座位。
#                   // 所以无法安排 2 个连续座位。
# bms.scatter(5, 1); // 返回 True
#                    // 这一组安排第 0 排第 4 个座位和第 1 排 [0, 3] 的座位。
# bms.scatter(5, 1); // 返回 False
#                    // 总共只剩下 2 个座位。
#  
#
# 提示：
#
# 1 <= n <= 5 * 104
# 1 <= m, k <= 109
# 0 <= maxRow <= n - 1
# gather 和 scatter 总 调用次数不超过 5 * 104 次。



from leetcode.allcode.competition.mypackage import *
import math

class BookMyShow:

    def pushup(self, pos):
        if pos == 0:
            return
        parents = pos // 2
        self.idle_num[parents] = max(self.idle_num[parents * 2], self.idle_num[parents * 2 + 1])
        self.sum_idle[parents] = self.sum_idle[parents * 2] + self.sum_idle[parents * 2 + 1]
        self.pushup(pos // 2)
    def pushdown(selfs, pos):
        pass
    def __init__(self, n: int, m: int):
        self.N = math.ceil(math.log(n, 2))
        self.m = m
        self.n = n
        self.idle_num = [0] * (2 ** (self.N + 1))
        self.sum_idle = [0] * (2 ** (self.N + 1))
        self.start = 2 ** self.N
        self.estart = self.start  # 有空闲的起始位置
        # self.left = n * m
        for i in range(self.start, self.start + n):
            self.idle_num[i] = m
            self.sum_idle[i] = m
            self.pushup(i)

    def query(self, maxRow, k):
        def helper(l, r, idx, k_):
            if idx >= self.start:
                return self.sum_idle[idx]
            if self.sum_idle[idx] < k_:
                return self.sum_idle[idx]
            mid = (l + r) // 2
            if maxRow > mid:
                s = helper(mid + 1, r, idx * 2 + 1, k_ - self.sum_idle[idx * 2])
                return self.sum_idle[idx * 2] + s
            else:
                return helper(l, mid, idx * 2, k_)
        # mm = self.n.bit_length
        # l, r = 0, (2 << (mm - 1)) - 1
        l, r = 0, 2 ** self.N - 1
        return helper(l, r, 1, k) >= k

    def gather(self, k: int, maxRow: int) -> List[int]:
        if self.idle_num[1] < k:
            return []
        pos = 1
        while self.idle_num[pos] >= k:
            if self.start <= pos <= self.start + maxRow:
                ans = [pos - self.start, self.m - self.idle_num[pos]]
                self.idle_num[pos] -= k
                self.sum_idle[pos] -= k
                self.pushup(pos)
                # self.left -= k
                return ans
            if pos >= self.start + maxRow:
                return []
            if self.idle_num[pos * 2] >= k:
                pos *= 2
            else:
                pos = pos * 2 + 1

    def scatter(self, k: int, maxRow: int) -> bool:
        if not self.query(maxRow, k):
            return False
        def helper(idx, k):
            if idx >= self.start:
                self.sum_idle[idx] -= k
                self.idle_num[idx] -= k
                self.pushup(idx)
                return
            # mid = (l + r) // 2
            if self.sum_idle[idx * 2] < k:
                k -= self.sum_idle[idx * 2]
                self.sum_idle[idx * 2] = 0
                self.idle_num[idx * 2] = 0
                self.pushup(idx * 2)
                # helper(mid + 1, r, idx * 2 + 1, k)
                helper(idx * 2 + 1, k)
                return
            # helper(l, mid, idx * 2, k)
            helper(idx * 2, k)
            return
        # l, r = 0, (2 << (self.n.bit_length - 1)) - 1
        # helper(l, r, 1, k)
        helper(1, k)
        return True









# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)

# ["BookMyShow","scatter","gather","gather","gather","scatter","scatter","scatter","scatter","gather","gather","gather"]
# [[19,9],[16,4],[24,8],[47,8],[36,13],[6,16],[3,0],[49,5],[12,11],[33,13],[18,6],[28,2]]
# [null,true,[],[],[],true,false,false,true,[],[],[]]
so = BookMyShow(19,9)      #
print(so.scatter(16,4))  # True
print(so.gather(24,8))  # []
print(so.gather(47,8))  # []
print(so.gather(36,13))  # []
print(so.scatter(6,16))  # True
print(so.scatter(3,0))  # False
print(so.scatter(49,5))  # False
print(so.scatter(12,11))  # True


print('NEXT')
# ["BookMyShow","gather","gather","scatter","scatter","gather","scatter","scatter","gather","scatter","scatter","gather","scatter","gather","scatter","gather","gather"]
# [[19,9],[38,8],[27,3],[36,14],[46,2],[12,5],[12,12],[43,12],[30,5],[29,6],[37,18],[6,16],[27,4],[4,17],[14,7],[11,5],[22,8]]

# [null,[],[],true,false,[],true,true,[],false,true,[14,2],false,[15,0],false,[],[]]
so = BookMyShow(19,9)      #
print(so.gather(38,8))  # []
print(so.gather(27,3))  # []
print(so.scatter(36,14))  # True
print(so.scatter(46,2))  # False
print(so.gather(12,5))  # []
print(so.scatter(12,12))  # True
print(so.scatter(43,12))  # True
print(so.gather(30,5))  # []
print(so.scatter(29,6))  # False
print(so.scatter(37,18))  # True
print(so.gather(6,16))  # [14,2]
print(so.scatter(27,4))  # False
print(so.gather(4,17))  # [15,0]
print(so.scatter(14,7))  # False
print(so.gather(11,5))  # []
print(so.gather(22,8))  # []

# []
# True
# [1, 0]
# []
# [0, 3]
so = BookMyShow(5, 9)
print(so.gather(10, 1))
print(so.scatter(3, 3))
print(so.gather(9, 1))
print(so.gather(10, 2))
print(so.gather(2, 0))

# [0, 0]
# []
# True
# False
so = BookMyShow(2, 5)
print(so.gather(4, 0))
print(so.gather(2, 0))
print(so.scatter(5, 1))
print(so.scatter(5, 1))

so = BookMyShow(2, 8)
print(so.scatter(3, 0))
print(so.gather(8, 0))

so = BookMyShow(5, 9)
print(so.gather(10, 1))
print(so.scatter(3, 3))
print(so.gather(9, 1))
print(so.gather(10, 2))
print(so.gather(2, 0))





