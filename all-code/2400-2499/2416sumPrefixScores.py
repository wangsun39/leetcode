# 给你一个长度为 n 的数组 words ，该数组由 非空 字符串组成。
#
# 定义字符串 word 的 分数 等于以 word 作为 前缀 的 words[i] 的数目。
#
# 例如，如果 words = ["a", "ab", "abc", "cab"] ，那么 "ab" 的分数是 2 ，因为 "ab" 是 "ab" 和 "abc" 的一个前缀。
# 返回一个长度为 n 的数组 answer ，其中 answer[i] 是 words[i] 的每个非空前缀的分数 总和 。
#
# 注意：字符串视作它自身的一个前缀。
#
#  
#
# 示例 1：
# 
# 输入：words = ["abc","ab","bc","b"]
# 输出：[5,4,3,2]
# 解释：对应每个字符串的答案如下：
# - "abc" 有 3 个前缀："a"、"ab" 和 "abc" 。
# - 2 个字符串的前缀为 "a" ，2 个字符串的前缀为 "ab" ，1 个字符串的前缀为 "abc" 。
# 总计 answer[0] = 2 + 2 + 1 = 5 。
# - "ab" 有 2 个前缀："a" 和 "ab" 。
# - 2 个字符串的前缀为 "a" ，2 个字符串的前缀为 "ab" 。
# 总计 answer[1] = 2 + 2 = 4 。
# - "bc" 有 2 个前缀："b" 和 "bc" 。
# - 2 个字符串的前缀为 "b" ，1 个字符串的前缀为 "bc" 。
# 总计 answer[2] = 2 + 1 = 3 。
# - "b" 有 1 个前缀："b"。
# - 2 个字符串的前缀为 "b" 。
# 总计 answer[3] = 2 。
# 示例 2：
#
# 输入：words = ["abcd"]
# 输出：[4]
# 解释：
# "abcd" 有 4 个前缀 "a"、"ab"、"abc" 和 "abcd"。
# 每个前缀的分数都是 1 ，总计 answer[0] = 1 + 1 + 1 + 1 = 4 。
#  
#
# 提示：
#
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 1000
# words[i] 由小写英文字母组成


from typing import List
from typing import Optional
from collections import deque
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
# 如果需要获取堆中最大或最小的范围值，则可以使用heapq.nlargest() 或heapq.nsmallest() 函数

# Map = [['U' for _ in range(n)] for _ in range(m)]

from functools import lru_cache
from typing import List
# @lru_cache(None)

# bit位 函数：
# n.bit_length()
# value = int(s, 2)

import string
# string.digits  表示 0123456789
# string.letters：包含所有字母(大写或小写字符串，在python3.0中，使用string.ascii-letters代替)
# string.lowercase：包含所有小写字母的字符串
# string.printable：包含所有可打印字符的字符串
# string.punctuation：包含所有标点的字符串
# string.uppercase：包含所有大写字母的字符串

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        d = defaultdict(int)
        for word in words:
            n = len(word)
            for i in range(n):
                d[word[:i + 1]] += 1
        ans = []
        for word in words:
            n = len(word)
            score = 0
            for i in range(n):
                score += d[word[:i + 1]]
            ans.append(score)
        return ans



so = Solution()
print(so.sumPrefixScores(words = ["abc","ab","bc","b"]))
# print(so.sumPrefixScores(words = ["abc","ab","bc","b"]))
print(so.sumPrefixScores(words = ["abcd"]))




