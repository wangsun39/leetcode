# X 轴上有一些机器人和工厂。给你一个整数数组 robot ，其中 robot[i] 是第 i 个机器人的位置。再给你一个二维整数数组 factory ，其中 factory[j] = [positionj, limitj] ，表示第 j 个工厂的位置在 positionj ，且第 j 个工厂最多可以修理 limitj 个机器人。
#
# 每个机器人所在的位置 互不相同 。每个工厂所在的位置也 互不相同 。注意一个机器人可能一开始跟一个工厂在 相同的位置 。
#
# 所有机器人一开始都是坏的，他们会沿着设定的方向一直移动。设定的方向要么是 X 轴的正方向，要么是 X 轴的负方向。当一个机器人经过一个没达到上限的工厂时，这个工厂会维修这个机器人，且机器人停止移动。
#
# 任何时刻，你都可以设置 部分 机器人的移动方向。你的目标是最小化所有机器人总的移动距离。
#
# 请你返回所有机器人移动的最小总距离。测试数据保证所有机器人都可以被维修。
#
# 注意：
#
# 所有机器人移动速度相同。
# 如果两个机器人移动方向相同，它们永远不会碰撞。
# 如果两个机器人迎面相遇，它们也不会碰撞，它们彼此之间会擦肩而过。
# 如果一个机器人经过了一个已经达到上限的工厂，机器人会当作工厂不存在，继续移动。
# 机器人从位置 x 到位置 y 的移动距离为 |y - x| 。
#
#
# 示例 1：
#
#
#
# 输入：robot = [0,4,6], factory = [[2,2],[6,2]]
# 输出：4
# 解释：如上图所示：
# - 第一个机器人从位置 0 沿着正方向移动，在第一个工厂处维修。
# - 第二个机器人从位置 4 沿着负方向移动，在第一个工厂处维修。
# - 第三个机器人在位置 6 被第二个工厂维修，它不需要移动。
# 第一个工厂的维修上限是 2 ，它维修了 2 个机器人。
# 第二个工厂的维修上限是 2 ，它维修了 1 个机器人。
# 总移动距离是 |2 - 0| + |2 - 4| + |6 - 6| = 4 。没有办法得到比 4 更少的总移动距离。
# 示例 2：
#
#
#
# 输入：robot = [1,-1], factory = [[-2,1],[2,1]]
# 输出：2
# 解释：如上图所示：
# - 第一个机器人从位置 1 沿着正方向移动，在第二个工厂处维修。
# - 第二个机器人在位置 -1 沿着负方向移动，在第一个工厂处维修。
# 第一个工厂的维修上限是 1 ，它维修了 1 个机器人。
# 第二个工厂的维修上限是 1 ，它维修了 1 个机器人。
# 总移动距离是 |2 - 1| + |(-2) - (-1)| = 2 。没有办法得到比 2 更少的总移动距离。
#
#
# 提示：
#
# 1 <= robot.length, factory.length <= 100
# factory[j].length == 2
# -109 <= robot[i], positionj <= 109
# 0 <= limitj <= robot.length
# 测试数据保证所有机器人都可以被维修。

import copy
from typing import List
from typing import Optional
from cmath import inf
from collections import deque
# de = deque([1, 2, 3])
# de.append(4)
# de.appendleft(6)
# de.pop()
# de.popleft()
from itertools import pairwise
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# d = defaultdict(int)
import math
import random
# random.uniform(a, b)，用于生成一个指定范围内的随机浮点数，闭区间
# randint和randrange的区别：
# randint 产生的随机数区间是包含左右极限的，也就是说左右都是闭区间的[1, n]，能取到1和n。
# 而 randrange 产生的随机数区间只包含左极限，也就是左闭右开的[1, n)，1能取到，而n取不到。

# 浮点数： price = "{:.02f}".format(price)
# newword = float(word[1:]) * (100 - discount) / 100
# newword = "%.2f" % newword
# a.isalpha()  # 判断字符串中是否所有的字符都是字母
# a.isdigit() # 判断字符串中是否所有的字符都是整数
# a.isalnum()  # 判断字符串中是否所有的字符都是字母or数字
# a.isspace()  # 判断字符串中是否所有的字符都是空白符
# a.swapcase()  # 转换大小写

import bisect
# bisect_right：
# 若序列a中存在与x相同的元素，则返回x相等元素右侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x左侧距离最近元素插入点的索引位置
# pos = bisect.bisect_right(left, tail)
# bisect_left：
# 若序列a中存在与x相同的元素，则返回x相等元素左侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x右侧距离最近元素插入点的索引位置
import heapq
# heap.heapify(nums) # 小顶堆
# heapq.heappop() 函数弹出堆中最小值
# heapq.heappush(nums, 1)
# heapq.heapreplace(heap, item)  删除最小值并添加新值
# 如果需要获取堆中最大或最小的范围值，则可以使用heapq.nlargest() 或heapq.nsmallest() 函数

# Map = [['U' for _ in range(n)] for _ in range(m)]

from functools import lru_cache, cache
from typing import List
# @lru_cache(None)

# bit位 函数：
# n.bit_length()  数值的二进制的长度数
# value = int(s, 2)
# lowbit(i) 即i&-i	返回i的最后一位1
# n>>k & 1	求n的第k位数字
# x | (1 << k)	将x第k位 置为1
# x ^ (1 << k)	将x第k位取反
# x & (x - 1)	将x最右边的1置为0(去掉最右边的1)
# x | (x + 1)	将x最右边的0置为1
# x & 1	判断奇偶性 真为奇，假为偶


import string
# string.digits  表示 0123456789
# string.letters：包含所有字母(大写或小写字符串，在python3.0中，使用string.ascii-letters代替)
# string.ascii_lowercase：包含所有小写字母的字符串
# string.printable：包含所有可打印字符的字符串
# string.punctuation：包含所有标点的字符串
# string.uppercase：包含所有大写字母的字符串

# f-string用法
# name = 'sun'
# f"Hello, my name is {name}"

from itertools import accumulate
# s = list(accumulate(nums, initial=0))  # 计算前缀和

from sortedcontainers import SortedList
    # SortedList.add(value) 添加新元素，并排序。时间复杂度O(log(n)).
    # SortedList.update(iterable) 对添加的可迭代的所有元素排序。时间复杂度O(k*log(n)).
    # SortedList.clear() 移除所有元素。时间复杂度O(n).
    # SortedList.discard(value) 移除一个值元素，如果元素不存在，不报错。时间复杂度O(log(n)).
    # SortedList.remove(value) 移除一个值元素，如果元素不存在，报错ValueError。时间复杂度O(log(n)).
    # SortedList.pop(index=-1) 移除一个指定下标元素，如果有序序列为空或者下标超限，报错IndexError.
    # SortedList.bisect_left(value)
    # SortedList.bisect_right(value)
    # SortedList.count(value)
    # SortedList.index(value, start=None, Stop=None) 查找索引范围[start,stop）内第一次出现value的索引，如果value不存在，报错ValueError.

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        def dfs(r, f):
            if len(r) == 0: return 0
            ans = 1e18
            for idx, ff in enumerate(f):
                cur = 0
                if ff[1] > 0:
                    cur += abs(r[0] - ff[0])
                    newf = copy.deepcopy(f)
                    newf[idx][1] -= 1
                    cur += dfs(r[1:], newf)
                    ans = min(ans, cur)
            return ans
        return dfs(robot, factory)


so = Solution()
print(so.minimumTotalDistance(robot = [0,4,6], factory = [[2,2],[6,2]]))




