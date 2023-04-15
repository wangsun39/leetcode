# 给你一个下标从 0 开始的二维整数数组 nums 。
#
# 返回位于 nums 至少一条 对角线 上的最大 质数 。如果任一对角线上均不存在质数，返回 0 。
#
# 注意：
#
# 如果某个整数大于 1 ，且不存在除 1 和自身之外的正整数因子，则认为该整数是一个质数。
# 如果存在整数 i ，使得 nums[i][i] = val 或者 nums[i][nums.length - i - 1]= val ，则认为整数 val 位于 nums 的一条对角线上。
#
#
# 在上图中，一条对角线是 [1,5,9] ，而另一条对角线是 [3,5,7] 。
#
#
#
# 示例 1：
#
# 输入：nums = [[1,2,3],[5,6,7],[9,10,11]]
# 输出：11
# 解释：数字 1、3、6、9 和 11 是所有 "位于至少一条对角线上" 的数字。由于 11 是最大的质数，故返回 11 。
# 示例 2：
#
# 输入：nums = [[1,2,3],[5,17,7],[9,11,10]]
# 输出：17
# 解释：数字 1、3、9、10 和 17 是所有满足"位于至少一条对角线上"的数字。由于 17 是最大的质数，故返回 17 。
#
#
# 提示：
#
# 1 <= nums.length <= 300
# nums.length == numsi.length
# 1 <= nums[i][j] <= 4*106

from typing import List
from typing import Optional
from cmath import inf
from collections import deque
# de = deque([1, 2, 3])
# de.append(4)
# de.appendleft(6)
# de.pop()
# de.popleft()
from itertools import pairwise, accumulate
# list(accumulate(nums))  数组前缀和
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# print(c.most_common(2)) # n = 2
#  [('c', 3), ('b', 2)]

# d = defaultdict(int)
from math import *
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

from bisect import *
# bisect_right：
# 若序列a中存在与x相同的元素，则返回x相等元素右侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x左侧距离最近元素插入点的索引位置
# pos = bisect.bisect_right(left, tail)
# bisect_left：
# 若序列a中存在与x相同的元素，则返回x相等元素左侧插入点的索引位置
# 若序列a中不存在与x相同的元素，则返回与x右侧距离最近元素插入点的索引位置
from heapq import *
# heap.heapify(nums) # 小顶堆
# heapq.heappop() 函数弹出堆中最小值
# heapq.heappush(nums, 1)
# heapq.heapreplace(heap, item)  删除最小值并添加新值
# 如果需要获取堆中最大或最小的范围值，则可以使用heapq.nlargest() 或heapq.nsmallest() 函数

# Map = [['U' for _ in range(n)] for _ in range(m)]
# Map = [['U'] * n for _ in range(m)]

from functools import lru_cache, cache
from typing import List, Tuple
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
# string.ascii_uppercase：包含所有大写字母的字符串
# string.printable：包含所有可打印字符的字符串
# string.punctuation：包含所有标点的字符串
# string.uppercase：包含所有大写字母的字符串

# f-string用法
# name = 'sun'
# f"Hello, my name is {name}"

from itertools import accumulate
# s = list(accumulate(nums, initial=0))  # 计算前缀和

from sortedcontainers import SortedList
    # sl = SortedList()
    # sl.add(value) 添加新元素，并排序。时间复杂度O(log(n)).
    # sl.update(iterable) 对添加的可迭代的所有元素排序。时间复杂度O(k*log(n)).
    # sl.clear() 移除所有元素。时间复杂度O(n).
    # sl.discard(value) 移除一个值元素，如果元素不存在，不报错。时间复杂度O(log(n)).
    # sl.remove(value) 移除一个值元素，如果元素不存在，报错ValueError。时间复杂度O(log(n)).
    # sl.pop(index=-1) 移除一个指定下标元素，如果有序序列为空或者下标超限，报错IndexError.
    # sl.bisect_left(value)
    # sl.bisect_right(value)
    # sl.count(value)
    # sl.index(value, start=None, Stop=None) 查找索引范围[start,stop）内第一次出现value的索引，如果value不存在，报错ValueError.

# 前缀和
# 左闭右开区间 [left,right) 来表示从 nums[left] 到 nums[right−1] 的子数组，
# 此时子数组的和为 s[right]−s[left]，子数组的长度为 right−left。
# s = list(accumulate(nums, initial=0))

# dir = [[-1, 0], [1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1], [0, -1], [0, 1]]
# dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]


class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        n = len(nums)
        ans = 0
        def check(x):
            if x <= 1: return False
            i = 2
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 1
            return True
        print(check(1))
        for i in range(n):
            if check(nums[i][i]):
                ans = max(ans, nums[i][i])
            if check(nums[i][n - i - 1]):
                ans = max(ans, nums[i][n - i - 1])
        return ans


so = Solution()
print(so.diagonalPrime(nums = [[395,777,912,431,42,266,989,524,498,415,941,803,850,311,992,489,367,598,914,930,224,517,143,289,144,774,98,634],[819,257,932,546,723,830,617,924,151,318,102,748,76,921,871,701,339,484,574,104,363,445,324,626,656,935,210,990],[566,489,454,887,534,267,64,825,941,562,938,15,96,737,861,409,728,845,804,685,641,2,627,506,848,889,342,250],[748,334,721,892,65,196,940,582,228,245,823,991,146,823,557,459,94,83,328,897,521,956,502,112,309,565,299,724],[128,561,341,835,945,554,209,987,819,618,561,602,295,456,94,611,818,395,325,590,248,298,189,194,842,192,34,628],[673,267,488,71,92,696,776,134,898,154,946,40,863,83,920,717,946,850,554,700,401,858,723,538,283,535,832,242],[870,221,917,696,604,846,973,430,594,282,462,505,677,657,718,939,813,366,85,333,628,119,499,602,646,344,866,195],[249,17,750,278,120,723,226,381,814,175,341,437,836,64,104,802,150,876,715,225,47,837,588,650,932,959,548,617],[697,76,28,128,651,194,621,851,590,123,401,94,380,854,119,38,621,23,200,985,994,190,736,127,491,216,745,820],[63,960,696,24,558,436,636,104,856,267,72,227,74,663,309,359,447,185,63,516,479,41,611,104,717,401,205,267],[368,927,750,482,859,924,941,584,174,715,689,209,990,786,60,808,693,163,866,166,351,543,257,121,612,944,453,682],[180,14,483,698,420,922,583,896,521,940,319,665,366,398,858,674,257,158,575,708,13,469,760,81,344,757,47,558],[288,139,246,781,977,494,361,625,295,690,368,605,970,914,649,875,636,136,733,318,398,767,425,849,667,83,2,609],[197,716,343,164,246,229,653,459,388,728,897,690,582,896,425,33,412,893,719,582,429,791,679,727,48,170,457,66],[266,719,162,458,541,907,499,930,575,619,774,1,906,40,507,334,320,858,479,52,829,843,897,998,832,426,193,562],[987,649,86,858,743,134,16,412,973,695,428,324,4,219,15,735,773,3,843,692,542,627,101,196,122,623,665,204],[895,310,287,706,187,103,488,875,945,407,643,84,23,282,936,464,820,812,119,883,263,137,670,534,837,667,661,356],[118,893,159,286,872,20,44,42,211,698,266,572,323,970,376,961,582,932,870,44,867,768,985,719,623,672,507,730],[660,925,470,656,446,382,893,551,183,213,385,602,299,10,142,155,278,342,346,809,377,736,96,347,799,636,37,43],[277,168,154,598,297,370,405,562,133,301,118,490,749,246,957,50,316,184,878,536,747,73,310,413,856,337,307,425],[112,102,575,931,493,486,346,862,818,1000,832,352,128,491,119,717,510,437,39,310,344,753,704,916,160,942,171,642],[579,385,826,998,655,90,68,828,87,203,768,227,63,395,9,101,404,570,532,297,460,943,501,808,599,732,696,223],[434,86,378,226,268,600,796,171,442,197,368,118,66,842,885,874,719,29,925,539,463,771,694,207,122,510,408,263],[213,657,44,971,817,222,639,150,108,203,470,388,371,560,847,155,108,611,500,152,578,416,654,697,434,899,534,508],[696,940,910,331,854,511,511,651,687,896,207,556,625,954,225,10,349,723,986,765,921,326,838,330,37,538,152,896],[264,618,803,160,863,389,597,302,736,724,827,482,68,820,87,529,890,938,41,68,231,134,42,308,16,778,865,460],[339,883,165,820,153,890,672,472,992,381,518,392,923,543,515,35,588,93,695,814,825,531,777,615,79,765,437,928],[773,212,297,549,923,613,428,846,996,494,866,811,996,398,623,601,240,872,886,818,21,673,907,1,759,187,310,520]]))
print(so.diagonalPrime(nums = [[1,2,3],[5,6,7],[9,10,11]]))
print(so.diagonalPrime(nums = [[1,2,3],[5,17,7],[9,11,10]]))




