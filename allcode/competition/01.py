

from leetcode.allcode.competition.mypackage import *

class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        r, c = 0, 0
        for com in commands:
            if com == 'UP':
                r -= 1
            elif com == 'RIGHT':
                c += 1
            elif com == 'DOWN':
                r += 1
            else:
                c -= 1
        return r * n + c


so = Solution()
print(so.finalPositionOfSnake(n = 2, commands = ["RIGHT","DOWN"]))
print(so.finalPositionOfSnake(n = 3, commands = ["DOWN","RIGHT","UP"]))




