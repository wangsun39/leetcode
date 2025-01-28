# 给你一个下标从 0开始的字符串数组nums，其中每个字符串 长度相等且只包含数字。
#
# 再给你一个下标从 0开始的二维整数数组queries，其中queries[i] = [ki, trimi]。对于每个queries[i]，你需要：
#
# 将nums中每个数字 裁剪到剩下 最右边trimi个数位。
# 在裁剪过后的数字中，找到 nums中第ki小数字对应的 下标。如果两个裁剪后数字一样大，那么下标 更小的数字视为更小的数字。
# 将 nums中每个数字恢复到原本字符串。
# 请你返回一个长度与 queries相等的数组answer，其中answer[i]是第i次查询的结果。
#
# 提示：
#
# 裁剪到剩下 x个数位的意思是不断删除最左边的数位，直到剩下 x个数位。
# nums中的字符串可能会有前导 0 。
#
#
# 示例 1：
#
# 输入：nums = ["102","473","251","814"], queries = [[1,1],[2,3],[4,2],[1,2]]
# 输出：[2,2,1,0]
# 解释：
# 1. 裁剪到只剩 1 个数位后，nums = ["2","3","1","4"] 。最小的数字是 1 ，下标为 2 。
# 2. 裁剪到剩 3 个数位后，nums 没有变化。第 2 小的数字是 251 ，下标为 2 。
# 3. 裁剪到剩 2 个数位后，nums = ["02","73","51","14"] 。第 4 小的数字是 73 ，下标为 1 。
# 4. 裁剪到剩 2 个数位后，最小数字是 2 ，下标为 0 。
#    注意，裁剪后数字 "02" 值为 2 。
# 示例 2：
#
# 输入：nums = ["24","37","96","04"], queries = [[2,1],[2,2]]
# 输出：[3,0]
# 解释：
# 1. 裁剪到剩 1 个数位，nums = ["4","7","6","4"] 。第 2 小的数字是 4 ，下标为 3 。
#    有两个 4 ，下标为 0 的 4 视为小于下标为 3 的 4 。
# 2. 裁剪到剩 2 个数位，nums 不变。第二小的数字是 24 ，下标为 0 。
#
#
# 提示：
#
# 1 <= nums.length <= 100
# 1 <= nums[i].length <= 100
# nums[i] 只包含数字。
# 所有nums[i].length的长度 相同。
# 1 <= queries.length <= 100
# queries[i].length == 2
# 1 <= ki <= nums.length
# 1 <= trimi <= nums[0].length


from typing import List
from typing import Optional
from collections import deque
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# d = defaultdict(int)
import random
# random.uniform(a, b)，用于生成一个指定范围内的随机浮点数，闭区间
# randint和randrange的区别：
# randint 产生的随机数区间是包含左右极限的，也就是说左右都是闭区间的[1, n]，能取到1和n。
# 而 randrange 产生的随机数区间只包含左极限，也就是左闭右开的[1, n)，1能取到，而n取不到。

# 浮点数： price = "{:.02f}".format(price)
# newword = float(word[1:]) * (100 - discount) / 100
# newword = "%.2f" % newword

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

# bit位 函数：
# n.bit_length()
# value = int(s, 2)

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        def query(k, trim):
            res = []
            for num in nums:
                res.append(num[-trim:])
            # print(res)
            newArray = [[i, e] for i, e in enumerate(res)]
            n = len(res)
            for i in range(n):
                for j in range(i, n):
                    if newArray[i][1] > newArray[j][1]:
                        newArray[i], newArray[j] = newArray[j], newArray[i]
                    elif newArray[i][1] == newArray[j][1] and newArray[i][0] > newArray[j][0]:
                        newArray[i], newArray[j] = newArray[j], newArray[i]


            # print(newArray, k)
            # print(newArray[k - 1], res.index(newArray[k - 1]))
            return newArray[k - 1][0]
        ans = []
        for qry in queries:
            idx = query(qry[0], qry[1])
            ans.append(idx)
        return ans




so = Solution()
# [1, 2, 11, 10, 7, 0, 0, 1, 13, 13, 2, 12]
print(so.smallestTrimmedNumbers(["64333639502","65953866768","17845691654","87148775908","58954177897","70439926174","48059986638","47548857440","18418180516","06364956881","01866627626","36824890579","14672385151","71207752868"], [[9,4],[6,1],[3,8],[12,9],[11,4],[4,9],[2,7],[10,3],[13,1],[13,1],[6,1],[5,10]]))
print(so.smallestTrimmedNumbers(nums = ["24","37","96","04"], queries = [[2,1],[2,2]]))
print(so.smallestTrimmedNumbers(nums = ["102","473","251","814"], queries = [[1,1],[2,3],[4,2],[1,2]]))




