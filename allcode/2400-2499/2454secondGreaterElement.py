# 给你一个下标从 0 开始的非负整数数组 nums 。对于 nums 中每一个整数，你必须找到对应元素的 第二大 整数。
#
# 如果 nums[j] 满足以下条件，那么我们称它为 nums[i] 的 第二大 整数：
#
# j > i
# nums[j] > nums[i]
# 恰好存在 一个 k 满足 i < k < j 且 nums[k] > nums[i] 。
# 如果不存在 nums[j] ，那么第二大整数为 -1 。
#
# 比方说，数组 [1, 2, 4, 3] 中，1 的第二大整数是 4 ，2 的第二大整数是 3 ，3 和 4 的第二大整数是 -1 。
# 请你返回一个整数数组 answer ，其中 answer[i]是 nums[i] 的第二大整数。
# 
#  
# 
# 示例 1：
# 
# 输入：nums = [2,4,0,9,6]
# 输出：[9,6,6,-1,-1]
# 解释：
# 下标为 0 处：2 的右边，4 是大于 2 的第一个整数，9 是第二个大于 2 的整数。
# 下标为 1 处：4 的右边，9 是大于 4 的第一个整数，6 是第二个大于 4 的整数。
# 下标为 2 处：0 的右边，9 是大于 0 的第一个整数，6 是第二个大于 0 的整数。
# 下标为 3 处：右边不存在大于 9 的整数，所以第二大整数为 -1 。
# 下标为 4 处：右边不存在大于 6 的整数，所以第二大整数为 -1 。
# 所以我们返回 [9,6,6,-1,-1] 。
# 示例 2：
# 
# 输入：nums = [3,3]
# 输出：[-1,-1]
# 解释：
# 由于每个数右边都没有更大的数，所以我们返回 [-1,-1] 。
#  
# 
# 提示：
# 
# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109
# https://leetcode.cn/problems/next-greater-element-iv/

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
    def secondGreaterElement1(self, nums: List[int]) -> List[int]: # 性能不够
        n = len(nums)
        array = []
        count = []
        ans = [-1] * n
        for i, num in enumerate(nums):
            pos = bisect.bisect_left(array, num, key=lambda x: x[0])
            array.insert(pos, [num, i])
            count.insert(pos, 0)
            for j in range(pos - 1, -1, -1):
                count[j] += 1
                if count[j] >= 2:
                    ans[array[j][1]] = num
                    del(array[j])
                    del(count[j])
        return ans

    def secondGreaterElement2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []
        queue = []
        for idx, num in enumerate(nums):
            while len(queue) and queue[-1][1] < num:
                ans[queue.pop()[0]] = num
            pos = len(stack) - 1
            while pos >= 0 and stack[pos][1] < num:
                pos -= 1
            queue += stack[pos + 1:]
            del(stack[pos + 1:])
            stack.append([idx, num])
            # print(queue)
        return ans

    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        # 2023/12/12 优先队列，性能不如上面的方法
        n = len(nums)
        ans = [-1] * n
        stack = []
        queue = []
        for idx, num in enumerate(nums):
            while len(queue) and queue[-1][1] < num:
                ans[queue.pop()[0]] = num
            pos = len(stack) - 1
            while pos >= 0 and stack[pos][1] < num:
                pos -= 1
            queue += stack[pos + 1:]
            del(stack[pos + 1:])
            stack.append([idx, num])
            # print(queue)
        return ans




so = Solution()
print(so.secondGreaterElement([11,13,15,12,0,15,12,11,9]))  # [15,15,-1,-1,12,-1,-1,-1,-1]
print(so.secondGreaterElement([8] * 49999 + [9] + [8] * 50000))

print(so.secondGreaterElement([2,4,0,9,6]))  # [9,6,6,-1,-1]
print(so.secondGreaterElement([7,7,7,8]))  # [-1, -1, -1, -1]
print(so.secondGreaterElement([1,17,18,0,18,10,20,0]))  # [18, 18, -1, 10, -1, -1, -1, -1]
print(so.secondGreaterElement(nums = [3,3]))  # [-1, -1]




