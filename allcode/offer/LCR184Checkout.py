# 请设计一个自助结账系统，该系统需要通过一个队列来模拟顾客通过购物车的结算过程，需要实现的功能有：
#
# get_max()：获取结算商品中的最高价格，如果队列为空，则返回 -1
# add(value)：将价格为 value 的商品加入待结算商品队列的尾部
# remove()：移除第一个待结算的商品价格，如果队列为空，则返回 -1
# 注意，为保证该系统运转高效性，以上函数的均摊时间复杂度均为 O(1)
#
#
#
# 示例 1：
#
# 输入:
# ["Checkout","add","add","get_max","remove","get_max"]
# [[],[4],[7],[],[],[]]
#
# 输出: [null,null,null,7,4,7]
# 示例 2：
#
# 输入:
# ["Checkout","remove","get_max"]
# [[],[],[]]
#
# 输出: [null,-1,-1]
#
#
# 提示：
#
# 1 <= get_max, add, remove 的总操作数 <= 10000
# 1 <= value <= 10^5

from leetcode.allcode.competition.mypackage import *


class Checkout:

    def __init__(self):
        self.dq = deque()
        self.hp = []
        self.deleted = Counter()

    def get_max(self) -> int:
        while self.hp:
            x = -self.hp[0]
            if self.deleted[x]:
                self.deleted[x] -= 1
                heappop(self.hp)
            else:
                break
        return -self.hp[0] if self.hp else -1

    def add(self, value: int) -> None:
        self.dq.append(value)
        heappush(self.hp, -value)

    def remove(self) -> int:
        if not self.dq: return -1
        x = self.dq.popleft()
        self.deleted[x] += 1
        return x


so = Checkout()




