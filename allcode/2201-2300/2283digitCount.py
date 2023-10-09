# 给你一个下标从 0 开始长度为 n 的字符串 num ，它只包含数字。
#
# 如果对于 每个 0 <= i < n 的下标 i ，都满足数位 i 在 num 中出现了 num[i]次，那么请你返回 true ，否则返回 false 。
#
#  
#
# 示例 1：
#
# 输入：num = "1210"
# 输出：true
# 解释：
# num[0] = '1' 。数字 0 在 num 中出现了一次。
# num[1] = '2' 。数字 1 在 num 中出现了两次。
# num[2] = '1' 。数字 2 在 num 中出现了一次。
# num[3] = '0' 。数字 3 在 num 中出现了零次。
# "1210" 满足题目要求条件，所以返回 true 。
# 示例 2：
#
# 输入：num = "030"
# 输出：false
# 解释：
# num[0] = '0' 。数字 0 应该出现 0 次，但是在 num 中出现了一次。
# num[1] = '3' 。数字 1 应该出现 3 次，但是在 num 中出现了零次。
# num[2] = '0' 。数字 2 在 num 中出现了 0 次。
# 下标 0 和 1 都违反了题目要求，所以返回 false 。
#  
#
# 提示：
#
# n == num.length
# 1 <= n <= 10
# num 只包含数字。


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
    def digitCount(self, num: str) -> bool:
        counter = Counter(num)
        print(counter)
        for i, s in enumerate(num):
            if counter[str(i)] != int(s):
                return False
        return True


so = Solution()
print(so.digitCount("1210"))
print(so.digitCount("030"))




