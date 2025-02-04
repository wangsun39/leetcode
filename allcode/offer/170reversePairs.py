# 在股票交易中，如果前一天的股价高于后一天的股价，则可以认为存在一个「交易逆序对」。请设计一个程序，输入一段时间内的股票交易记录 record，返回其中存在的「交易逆序对」总数。
# 
#  
# 
# 示例 1:
# 
# 输入：record = [9, 7, 5, 4, 6]
# 输出：8
# 解释：交易中的逆序对为 (9, 7), (9, 5), (9, 4), (9, 6), (7, 5), (7, 4), (7, 6), (5, 4)。
#  
# 
# 限制：
# 
# 0 <= record.length <= 50000


from leetcode.allcode.competition.mypackage import *



class Solution1:
    def reversePairs(self, record: List[int]) -> int:
        # 二分解法
        sl = SortedList()
        ans = 0
        for x in record:
            p = sl.bisect_right(x)
            ans += (len(sl) - p)
            sl.add(x)
        return ans

class Fenwick:
    # 所有函数参数下标从1开始，可以传入使用者的数值x+1的值
    __slots__ = ['f', 'nums']

    def __init__(self, n: int):
        # n 是能调用下面函数的下标最大值
        self.f = [0] * (n + 1)  # 关键区间
        self.nums = [0] * (n + 1)

    def add(self, i: int, val: int) -> None:  # nums[i] += val
        self.nums[i] += val
        while i < len(self.f):
            self.f[i] += val
            i += i & -i

    def update(self, i: int, val: int) -> None:  # nums[i] += val
        delta = val - self.nums[i]
        self.add(i, delta)

    def pre(self, i: int) -> int:  # 下标<=i的和
        res = 0
        while i > 0:
            res += self.f[i]
            i &= i - 1
        return res

    def query_one(self, idx: int):
        return self.nums[idx]

    def query(self, l: int, r: int) -> int:  # [l, r]  区间求和
        if r < l:
            return 0
        return self.pre(r) - self.pre(l - 1)


class Solution:
    def reversePairs(self, record: List[int]) -> int:
        # 2025/2/3 树状数组解法
        if len(record) == 0: return 0
        rr = []
        for i, x in sorted(enumerate(record), key=lambda x: x[1]):
            rr.append(i + 1)
        mx = len(rr)
        fw = Fenwick(mx)
        ans = 0
        for x in rr:
            if x + 1 <= mx:
                ans += fw.query(x + 1, mx)
            fw.add(x, 1)

        return ans

so = Solution()
print(so.reversePairs([9, 7, 5, 4, 6]))




