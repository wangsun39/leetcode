# 给定循环单调非递减列表中的一个点，写一个函数向这个列表中插入一个新元素 insertVal ，使这个列表仍然是循环升序的。
#
# 给定的可以是这个列表中任意一个顶点的指针，并不一定是这个列表中最小元素的指针。
#
# 如果有多个满足条件的插入位置，可以选择任意一个位置插入新的值，插入后整个列表仍然保持有序。
#
# 如果列表为空（给定的节点是 null），需要创建一个循环有序列表并返回这个节点。否则。请返回原先给定的节点。
#
#  
#
# 示例 1：
#
#
#  
#
# 输入：head = [3,4,1], insertVal = 2
# 输出：[3,4,1,2]
# 解释：在上图中，有一个包含三个元素的循环有序列表，你获得值为 3 的节点的指针，我们需要向表中插入元素 2 。新插入的节点应该在 1 和 3 之间，插入之后，整个列表如上图所示，最后返回节点 3 。
#
#
# 示例 2：
#
# 输入：head = [], insertVal = 1
# 输出：[1]
# 解释：列表为空（给定的节点是 null），创建一个循环有序列表并返回这个节点。
# 示例 3：
#
# 输入：head = [1], insertVal = 0
# 输出：[1,0]
#  
#
# 提示：
#
# 0 <= Number of Nodes <= 5 * 10^4
# -10^6 <= Node.val <= 10^6
# -10^6 <= insertVal <= 10^6


from typing import List
from collections import deque
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# d = defaultdict(int)
#import random
# random.uniform(a, b)，用于生成一个指定范围内的随机浮点数，闭区间
# randint和randrange的区别：
# randint 产生的随机数区间是包含左右极限的，也就是说左右都是闭区间的[1, n]，能取到1和n。
# 而 randrange 产生的随机数区间只包含左极限，也就是左闭右开的[1, n)，1能取到，而n取不到。

# 浮点数： price = "{:.02f}".format(price)

import bisect
# bisect_right：
# 若序列a中存在与x相同的元素，则返回x相等元素右侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x左侧距离最近元素插入点的索引位置
# pos = bisect.bisect_right(left, tail)
# bisect_left：
# 若序列a中存在与x相同的元素，则返回x相等元素左侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x右侧距离最近元素插入点的索引位置

# Map = [['U' for _ in range(n)] for _ in range(m)]

from functools import lru_cache
from typing import List
# @lru_cache(None)

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if head is None:
            node = Node(insertVal)
            node.next = node
            return node
        cur = head.next
        while True:
            if cur.val == insertVal or cur.val < insertVal < cur.next.val:
                target = cur
                break
            if cur.val > cur.next.val > insertVal or insertVal > cur.val > cur.next.val:
                target = cur
                break
            if cur == head:
                target = cur
                break
            cur = cur.next
        t = target.next
        target.next = Node(insertVal)
        target.next.next = t
        return head


node = Node(3)
node.next = Node(4)
node.next.next = Node(1)
node.next.next.next = node
so = Solution()
print(so.insert(node, 2))




