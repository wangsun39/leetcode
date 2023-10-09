# 设计一个数据结构，有效地找到给定子数组的 多数元素 。
#
# 子数组的 多数元素 是在子数组中出现 threshold 次数或次数以上的元素。
#
# 实现 MajorityChecker 类:
#
# MajorityChecker(int[] arr) 会用给定的数组 arr 对 MajorityChecker 初始化。
# int query(int left, int right, int threshold) 返回子数组中的元素  arr[left...right] 至少出现 threshold 次数，如果不存在这样的元素则返回 -1。
#
#
# 示例 1：
#
# 输入:
# ["MajorityChecker", "query", "query", "query"]
# [[[1, 1, 2, 2, 1, 1]], [0, 5, 4], [0, 3, 3], [2, 3, 2]]
# 输出：
# [null, 1, -1, 2]
#
# 解释：
# MajorityChecker majorityChecker = new MajorityChecker([1,1,2,2,1,1]);
# majorityChecker.query(0,5,4); // 返回 1
# majorityChecker.query(0,3,3); // 返回 -1
# majorityChecker.query(2,3,2); // 返回 2
#
#
# 提示：
#
# 1 <= arr.length <= 2 * 104
# 1 <= arr[i] <= 2 * 104
# 0 <= left <= right < arr.length
# threshold <= right - left + 1
# 2 * threshold > right - left + 1
# 调用 query 的次数最多为 104
from random import randint
from typing import List, Optional
from collections import deque, defaultdict
from functools import cache
from bisect import *


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.stat = defaultdict(list)
        for i, x in enumerate(arr):
            self.stat[x].append(i)


    def query(self, left: int, right: int, threshold: int) -> int:
        for _ in range(20): # 进行 20 次随机选择
            r = self.arr[randint(left, right)]  # 计算随机数在区间内出现的次数
            n = right - left + 1
            mi = bisect_left(self.stat[r], left)
            mx = bisect_right(self.stat[r], right)
            t = mx - mi
            if t >= threshold:
                return r
            elif t * 2 >= n:
                return -1
        return -1


# ["MajorityChecker","query","query","query","query","query","query","query","query","query","query"]
# [[[2,2,1,2,1,2,2,1,1,2]],[2,5,4],[0,5,6],[0,1,2],[2,3,2],[6,6,1],[0,3,3],[4,9,6],[4,8,4],[5,9,5],[0,1,2]]

# Your MajorityChecker object will be instantiated and called as such:
obj = MajorityChecker([2,2,1,2,1,2,2,1,1,2])
print(obj.query(0,1,2))

obj = MajorityChecker([1, 1, 2, 2, 1, 1])
print(obj.query(0, 5, 4))
print(obj.query(0, 3, 3))
print(obj.query(2, 3, 2))


