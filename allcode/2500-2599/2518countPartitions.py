# 给你一个正整数数组 nums 和一个整数 k 。
#
# 分区 的定义是：将数组划分成两个有序的 组 ，并满足每个元素 恰好 存在于 某一个 组中。如果分区中每个组的元素和都大于等于 k ，则认为分区是一个好分区。
#
# 返回 不同 的好分区的数目。由于答案可能很大，请返回对 109 + 7 取余 后的结果。
#
# 如果在两个分区中，存在某个元素 nums[i] 被分在不同的组中，则认为这两个分区不同。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3,4], k = 4
# 输出：6
# 解释：好分区的情况是 ([1,2,3], [4]), ([1,3], [2,4]), ([1,4], [2,3]), ([2,3], [1,4]), ([2,4], [1,3]) 和 ([4], [1,2,3]) 。
# 示例 2：
#
# 输入：nums = [3,3,3], k = 4
# 输出：0
# 解释：数组中不存在好分区。
# 示例 3：
#
# 输入：nums = [6,6], k = 2
# 输出：2
# 解释：可以将 nums[0] 放入第一个分区或第二个分区中。
# 好分区的情况是 ([6], [6]) 和 ([6], [6]) 。
#
#
# 提示：
#
# 1 <= nums.length, k <= 1000
# 1 <= nums[i] <= 109

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
# lowbit(i) 即i&-i	表示这个数的二进制表示中最低位的1所对应的值
# n>>k & 1	求n的第k位数字
# x | (1 << k)	将x第k位 置为1
# x ^ (1 << k)	将x第k位取反
# x & (x - 1)	将x最右边的1置为0(去掉最右边的1)
# x | (x + 1)	将x最右边的0置为1
# x & 1	判断奇偶性 真为奇，假为偶

# x / y 上取整 (x + y - 1) // y
# x / y 下取整 x // y
# x / y 四舍五入 int(x / y + 0.5)

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
    def countPartitions1(self, nums: List[int], k: int) -> int:
        if sum(nums) < k * 2: return 0
        MOD = 10 ** 9 + 7
        n = len(nums)
        pre = [1 if i + 1 <= nums[0] else 2 for i in range(k)]  # 1 表示空集，2表示空集 + {nums[0]}
        # print(pre)
        dp = [0] * k  # dp[j] 子集的和小于 j+1 的子集个数
        for i in range(1, n):
            for j in range(k):
                if j >= nums[i]:
                    dp[j] = pre[j - nums[i]] + pre[j]
                    dp[j] %= MOD
                else:
                    dp[j] = pre[j]
            pre, dp = dp, [0] * k
            # print(pre)
        return ((pow(2, n, MOD) + MOD) - pre[-1] * 2) % MOD

    def countPartitions(self, nums: List[int], k: int) -> int:
        # 2023/1/30 重新写了一遍
        MOD = 10 ** 9 + 7
        s = sum(nums)
        if s < 2 * k: return 0
        n = len(nums)
        dp = [[0] * (1000) for _ in range(n)]  # dp[i][j]  前 i + 1 个数中和 == j 的子集个数
        dp[0][0] = 1   # 空集
        if nums[0] < 1000: dp[0][nums[0]] = 1
        for i in range(1, n):
            for j in range(1000):
                dp[i][j] = dp[i - 1][j]
                if nums[i] <= j:
                    dp[i][j] += dp[i - 1][j - nums[i]]
        total = pow(2, n, MOD) + MOD
        return (total - sum(dp[-1][:k]) * 2) % MOD


so = Solution()
print(so.countPartitions(nums = [6,6], k = 2))  # 2
print(so.countPartitions(nums = [3,3,3], k = 4))  # 0
print(so.countPartitions(nums = [1,2,3,4], k = 4))  # 6




