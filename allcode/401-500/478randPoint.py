# 给定圆的半径和圆心的位置，实现函数 randPoint ，在圆中产生均匀随机点。
#
# 实现 Solution 类:
#
# Solution(double radius, double x_center, double y_center) 用圆的半径 radius 和圆心的位置 (x_center, y_center) 初始化对象
# randPoint() 返回圆内的一个随机点。圆周上的一点被认为在圆内。答案作为数组返回 [x, y] 。
#  
#
# 示例 1：
#
# 输入:
# ["Solution","randPoint","randPoint","randPoint"]
# [[1.0, 0.0, 0.0], [], [], []]
# 输出: [null, [-0.02493, -0.38077], [0.82314, 0.38945], [0.36572, 0.17248]]
# 解释:
# Solution solution = new Solution(1.0, 0.0, 0.0);
# solution.randPoint ();//返回[-0.02493，-0.38077]
# solution.randPoint ();//返回[0.82314,0.38945]
# solution.randPoint ();//返回[0.36572,0.17248]
#  
#
# 提示：
#
# 0 < radius <= 108
# -107 <= x_center, y_center <= 107
# randPoint 最多被调用 3 * 104 次




import time
import random
import math

from typing import List
import copy
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x0 = x_center
        self.y0 = y_center
        self.r = radius


    def randPoint1(self) -> List[float]:
        while True:
            x, y = random.uniform(-self.r, self.r), random.uniform(-self.r, self.r)
            if x * x + y * y <= self.r * self.r:
                return [self.x0 + x, self.y0 + y]
    def randPoint(self) -> List[float]:
        # 2024/7/16  半径的平方上随机
        while True:
            d = random.uniform(0, self.r ** 2) ** 0.5
            arg = random.uniform(0, math.pi * 2)
            x = self.x0 + d * math.cos(arg)
            y = self.y0 + d * math.sin(arg)
            if (x - self.x0) ** 2 + (y - self.y0) ** 2 <= self.r ** 2:
                return [x, y]


so = Solution(1.0, 0.0, 0.0)

print(so.randPoint())



