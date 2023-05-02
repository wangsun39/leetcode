# 给定三个整数 x 、 y 和 bound ，返回 值小于或等于 bound 的所有 强整数 组成的列表 。
#
# 如果某一整数可以表示为 xi + yj ，其中整数 i >= 0 且 j >= 0，那么我们认为该整数是一个 强整数 。
#
# 你可以按 任何顺序 返回答案。在你的回答中，每个值 最多 出现一次。
#
#
#
# 示例 1：
#
# 输入：x = 2, y = 3, bound = 10
# 输出：[2,3,4,5,7,9,10]
# 解释：
# 2 = 20 + 30
# 3 = 21 + 30
# 4 = 20 + 31
# 5 = 21 + 31
# 7 = 22 + 31
# 9 = 23 + 30
# 10 = 20 + 32
# 示例 2：
#
# 输入：x = 3, y = 5, bound = 15
# 输出：[2,4,6,8,10,14]
#
#
# 提示：
#
# 1 <= x, y <= 100
# 0 <= bound <= 106
from math import log
from typing import List
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound == 0: return []
        mx_x, mx_y = bound if x > 1 else 0,  bound if y > 1 else 0
        ans = set()
        for i in range(mx_x + 1):
            l = x ** i
            if l > bound: break
            for j in range(mx_y + 1):
                cur = l + y ** j
                if cur > bound:
                    break
                ans.add(cur)
        return list(ans)



so = Solution()
print(so.powerfulIntegers(x = 1, y = 1, bound = 400000))
print(so.powerfulIntegers(x = 1, y = 1, bound = 0))
print(so.powerfulIntegers(x = 2, y = 1, bound = 10))
print(so.powerfulIntegers(x = 2, y = 3, bound = 10))
print(so.powerfulIntegers(x = 3, y = 5, bound = 15))

