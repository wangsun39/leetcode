# 给你一个聊天记录，共包含 n 条信息。给你两个字符串数组 messages 和 senders ，其中 messages[i] 是 senders[i] 发出的一条 信息 。
#
# 一条 信息 是若干用单个空格连接的 单词 ，信息开头和结尾不会有多余空格。发件人的 单词计数 是这个发件人总共发出的 单词数 。注意，一个发件人可能会发出多于一条信息。
#
# 请你返回发出单词数 最多 的发件人名字。如果有多个发件人发出最多单词数，请你返回 字典序 最大的名字。
#
# 注意：
#
# 字典序里，大写字母小于小写字母。
# "Alice" 和 "alice" 是不同的名字。
#  
#
# 示例 1：
#
# 输入：messages = ["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"], senders = ["Alice","userTwo","userThree","Alice"]
# 输出："Alice"
# 解释：Alice 总共发出了 2 + 3 = 5 个单词。
# userTwo 发出了 2 个单词。
# userThree 发出了 3 个单词。
# 由于 Alice 发出单词数最多，所以我们返回 "Alice" 。
# 示例 2：
#
# 输入：messages = ["How is leetcode for everyone","Leetcode is useful for practice"], senders = ["Bob","Charlie"]
# 输出："Charlie"
# 解释：Bob 总共发出了 5 个单词。
# Charlie 总共发出了 5 个单词。
# 由于最多单词数打平，返回字典序最大的名字，也就是 Charlie 。
#  
#
# 提示：
#
# n == messages.length == senders.length
# 1 <= n <= 104
# 1 <= messages[i].length <= 100
# 1 <= senders[i].length <= 10
# messages[i] 包含大写字母、小写字母和 ' ' 。
# messages[i] 中所有单词都由 单个空格 隔开。
# messages[i] 不包含前导和后缀空格。
# senders[i] 只包含大写英文字母和小写英文字母。

from typing import List
from collections import deque
# Definition for a binary tree node.
from collections import Counter
from collections import defaultdict
# d = Counter(list1)
# d = defaultdict(int)


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

class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        n = len(messages)
        d = defaultdict(int)
        for i in range(n):
            d[senders[i]] += (messages[i].count(' ') + 1)
        people = []
        maxNum = max(d.values())
        for k in d:
            if d[k] == maxNum:
                people.append(k)
        people.sort()
        print(people)
        return people[-1]



so = Solution()
print(so.largestWordCount(messages = ["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"], senders = ["Alice","userTwo","userThree","Alice"]))
print(so.largestWordCount(messages = ["How is leetcode for everyone","Leetcode is useful for practice"], senders = ["Bob","Charlie"]))




