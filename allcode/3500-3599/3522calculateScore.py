# 给你两个数组：instructions 和 values，数组的长度均为 n。
#
# 你需要根据以下规则模拟一个过程：
#
# 从下标 i = 0 的第一个指令开始，初始得分为 0。
# 如果 instructions[i] 是 "add"：
# 将 values[i] 加到你的得分中。
# 移动到下一个指令 (i + 1)。
# 如果 instructions[i] 是 "jump"：
# 移动到下标为 (i + values[i]) 的指令，但不修改你的得分。
# 当以下任一情况发生时，过程会终止：
#
# 越界（即 i < 0 或 i >= n），或
# 尝试再次执行已经执行过的指令。被重复访问的指令不会再次执行。
# 返回过程结束时的得分。
#
#
#
# 示例 1：
#
# 输入： instructions = ["jump","add","add","jump","add","jump"], values = [2,1,3,1,-2,-3]
#
# 输出： 1
#
# 解释：
#
# 从下标 0 开始模拟过程：
#
# 下标 0：指令是 "jump"，移动到下标 0 + 2 = 2。
# 下标 2：指令是 "add"，将 values[2] = 3 加到得分中，移动到下标 3。得分变为 3。
# 下标 3：指令是 "jump"，移动到下标 3 + 1 = 4。
# 下标 4：指令是 "add"，将 values[4] = -2 加到得分中，移动到下标 5。得分变为 1。
# 下标 5：指令是 "jump"，移动到下标 5 + (-3) = 2。
# 下标 2：已经访问过。过程结束。
# 示例 2：
#
# 输入： instructions = ["jump","add","add"], values = [3,1,1]
#
# 输出： 0
#
# 解释：
#
# 从下标 0 开始模拟过程：
#
# 下标 0：指令是 "jump"，移动到下标 0 + 3 = 3。
# 下标 3：越界。过程结束。
# 示例 3：
#
# 输入： instructions = ["jump"], values = [0]
#
# 输出： 0
#
# 解释：
#
# 从下标 0 开始模拟过程：
#
# 下标 0：指令是 "jump"，移动到下标 0 + 0 = 0。
# 下标 0：已经访问过。过程结束。
#
#
# 提示：
#
# n == instructions.length == values.length
# 1 <= n <= 105
# instructions[i] 只能是 "add" 或 "jump"。
# -105 <= values[i] <= 105

from leetcode.allcode.competition.mypackage import *

class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        n = len(instructions)
        vis = set()
        ans = 0
        i = 0
        while 0 <= i < n:
            if i in vis: break
            vis.add(i)
            if instructions[i] == 'add':
                ans += values[i]
                i += 1
            else:
                i += values[i]

        return ans


so = Solution()
print(so.calculateScore(instructions = ["jump","jump","add","jump","add","add","add","jump","add","jump","add","add","add","jump","jump","add","add","jump","add","add","add","jump","add","add","add","add","add","jump","add","jump","jump","jump","add","jump","jump","jump","add","jump","add","jump","jump","jump","jump","jump","jump","add","add","add","add","add","add","jump","jump","jump","add","add"], values = [12,18,-33551,4,70707,20722,-22225,23,-56668,-8,-7875,21146,26804,17,1,-13898,80265,22,-10903,38444,-69303,17,85973,-94700,-93741,56346,25785,-22,21628,12,-31893,70229,-78933,-14,20952,28335,-78481,7,33449,-17,-27011,-23,-29791,71663,-18,38373,48282,611,-65558,76770,49926,94315,-27,-3,14623,-67134]))
print(so.calculateScore(instructions = ["jump","add","add","jump","add","jump"], values = [2,1,3,1,-2,-3]))




